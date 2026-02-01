import os
import httplib2
from googleapiclient.discovery import build
from google.oauth2 import service_account

# --- НАСТРОЙКИ ---
JSON_KEY = "credentials.json"  # Твой ключ
URLS_FILE = "urls.txt"         # Список на отправку
HISTORY_FILE = "sent_history.txt" # Сюда будем писать то, что уже ушло

def run_smart_indexing():
    # 1. Проверки
    if not os.path.exists(JSON_KEY):
        print(f"[❌] Нет файла ключа: {JSON_KEY}")
        return
    if not os.path.exists(URLS_FILE):
        print(f"[❌] Нет файла ссылок: {URLS_FILE}")
        return

    # 2. Читаем ссылки
    with open(URLS_FILE, "r", encoding="utf-8") as f:
        all_urls = [line.strip() for line in f if line.strip()]

    if not all_urls:
        print("[🎉] Список пуст! Все ссылки уже отправлены.")
        return

    print(f"[📂] В очереди: {len(all_urls)} ссылок.")

    # 3. Авторизация в Google
    try:
        creds = service_account.Credentials.from_service_account_file(
            JSON_KEY, scopes=["https://www.googleapis.com/auth/indexing"]
        )
        service = build("indexing", "v3", credentials=creds)
    except Exception as e:
        print(f"[❌] Ошибка входа (проверь JSON): {e}")
        return

    # 4. Отправка (Лимит 200)
    batch = all_urls[:200]  # Берем первые 200
    remaining = all_urls[200:] # Остальные оставляем на завтра
    
    print(f"--- Заряжаю {len(batch)} ссылок... ---")
    
    success_count = 0
    for url in batch:
        body = {"url": url, "type": "URL_UPDATED"}
        try:
            service.urlNotifications().publish(body=body).execute()
            print(f"[🚀] Ушло: {url}")
            success_count += 1
        except Exception as e:
            error_msg = str(e)
            if "403" in error_msg:
                print(f"[⛔] ОШИБКА 403: Ты не добавил Email в 'Владельцы' Search Console!")
                return # Останавливаем, чтобы ты исправил
            elif "429" in error_msg:
                print(f"[⏳] Лимит исчерпан. Google говорит 'Хватит'.")
                break
            else:
                print(f"[⚠️] Сбой: {e}")

    # 5. Сохранение результата
    # Переписываем urls.txt (оставляем только то, что НЕ отправили)
    # Если была ошибка 429 (лимит), мы не удаляем неотправленные
    if success_count > 0:
        # Сохраняем остаток
        # (Если прервали по ошибке, сохраняем и те что не успели, и остаток)
        leftover = all_urls[success_count:] 
        
        with open(URLS_FILE, "w", encoding="utf-8") as f:
            for url in leftover:
                f.write(url + "\n")
        
        # Пишем в историю
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            for url in batch[:success_count]:
                f.write(url + "\n")

        print("-" * 30)
        print(f"[✅] УСПЕХ: Отправлено {success_count} ссылок.")
        print(f"[📉] Осталось в очереди: {len(leftover)}")
        print(f"[💾] Очередь обновлена. Завтра просто запусти скрипт снова.")

if __name__ == "__main__":
    run_smart_indexing()
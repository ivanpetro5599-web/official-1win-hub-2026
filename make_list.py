import os

# --- НАСТРОЙКИ ---
DOMAIN = "https://ivanpetro5599-web.github.io/official-1win-hub-2026"
FOLDER = "dist"

def create_url_list():
    print(f"--- ДИАГНОСТИКА ПУТИ ---")
    print(f"[📍] Текущая папка: {os.getcwd()}")

    # 1. Проверяем папку
    if not os.path.exists(FOLDER):
        print(f"[❌] ОШИБКА: Папка '{FOLDER}' не найдена!")
        print(f"👉 Решение: Сначала запусти 'python seo_machine.py'")
        return

    # 2. Пытаемся собрать файлы
    try:
        files = [f for f in os.listdir(FOLDER) if f.endswith(".html")]
        
        if not files:
            print(f"[⚠️] ВНИМАНИЕ: Папка '{FOLDER}' пустая. HTML файлов нет.")
            return

        with open("urls.txt", "w", encoding="utf-8") as f:
            for file in files:
                f.write(f"{DOMAIN.rstrip('/')}/{file}\n")
        
        print(f"[✅] УСПЕХ! Собрано ссылок: {len(files)}")
        print(f"[📄] Список сохранен в: urls.txt")

    except PermissionError:
        print(f"[❌] ОШИБКА: Файл urls.txt открыт в другой программе. Закрой его!")
    except Exception as e:
        print(f"[❓] ЧТО-ТО ПОШЛО НЕ ТАК: {e}")

if __name__ == "__main__":
    create_url_list()
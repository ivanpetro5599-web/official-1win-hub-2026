import os
import shutil

# --- НАСТРОЙКИ ---
SOURCE_DIR = "dist"
# Твоя ссылка
REPO_URL = "https://github.com/ivanpetro5599-web/official-1win-hub-2026.git"

# Файлы, которые НИКОГДА нельзя отправлять
IGNORE_FILES = """
credentials.json
sent_history.txt
github_pbn_factory.py
__pycache__
*.pyc
"""

def deploy_to_github():
    print("--- 🚀 БЕЗОПАСНАЯ ОТПРАВКА НА GITHUB ---")

    # 1. Создаем .gitignore (ЗАЩИТА ОТ ВЗЛОМА)
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(IGNORE_FILES.strip())
    print("[🔒] Файл .gitignore создан. Секреты под защитой.")

    # 2. Перенос файлов
    if os.path.exists(SOURCE_DIR):
        files = os.listdir(SOURCE_DIR)
        print(f"[📦] Перемещаю {len(files)} файлов в корень...")
        for file in files:
            if file.endswith(".html"):
                shutil.copy(os.path.join(SOURCE_DIR, file), file)
    
    # 3. Инициализация (если удалил .git)
    if not os.path.exists(".git"):
        print("[🔧] Инициализирую новый Git...")
        os.system("git init")
        os.system("git branch -M main")
        os.system(f"git remote add origin {REPO_URL}")

    # 4. Отправка
    try:
        print("[1/3] Git Add (Добавляю безопасные файлы)...")
        os.system("git add .")
        
        print("[2/3] Git Commit...")
        os.system('git commit -m "Site update (Secured)"')
        
        print("[3/3] Git Push (Force)...")
        push_code = os.system("git push -u origin main --force")
        
        if push_code == 0:
            print("-" * 30)
            print("[🎉] ПОБЕДА! Сайт обновлен, ключи остались дома.")
        else:
            print("[❌] Ошибка. Если GitHub ругается, убедись, что удалил папку .git перед запуском.")

    except Exception as e:
        print(f"[❌] Сбой: {e}")

if __name__ == "__main__":
    deploy_to_github()
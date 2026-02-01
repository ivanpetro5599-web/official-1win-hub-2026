import os

# Твоя ссылка на репозиторий
REPO_URL = "https://github.com/ivanpetro5599-web/official-1win-hub-2026.git"

def fix_github_pages():
    print("--- 🔧 ЛЕЧЕНИЕ GITHUB PAGES (404 ERROR) ---")

    # 1. Создаем пустой файл .nojekyll
    # Это отключает движок Jekyll, который часто ломает простые сайты
    with open(".nojekyll", "w") as f:
        f.write("")
    print("[✅] Файл .nojekyll создан (Jekyll отключен).")

    # 2. Пересоздаем index.html (на всякий случай, простой и надежный)
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>OFFICIAL MIRROR 2026</title></head>
    <body>
        <h1>ACCESS GRANTED ✅</h1>
        <p>This is the official gateway.</p>
        <a href="page-1.html"><h3>CLICK HERE TO ENTER</h3></a>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("[✅] Главная страница index.html обновлена.")

    # 3. Отправляем исправления на сервер
    print("--- ОТПРАВКА ---")
    os.system("git add .")
    os.system('git commit -m "Fix 404 error: Add nojekyll"')
    os.system("git push")
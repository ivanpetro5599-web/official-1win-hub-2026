import os
import subprocess

# --- КОНФИГУРАЦИЯ ---
GITHUB_USER = "ТВОЙ_ЛОГИН_GITHUB"
GITHUB_TOKEN = "ТВОЙ_ТОКЕН_ИЗ_НАСТРОЕК" # Тот самый PAT
REPO_NAME = "mirror-hub-2026"          # Имя сайта (любое)
REF_LINK = "ТВОЯ_ССЫЛКА_ИЗ_COLAB"      # Твой "якорь"

# Список ключей (можешь загрузить из keywords.txt)
KEYWORDS = ["1win mirror official", "1win india login", "1win registration bonus"]

def generate_html(key):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8"><title>{key.upper()} 2026</title></head>
    <body style="font-family: Arial; text-align: center; padding-top: 100px;">
        <h1>{key.upper()} - Official Mirror</h1>
        <p>Looking for verified access? Click the button below:</p>
        <a href="{REF_LINK}" style="background: #28a745; color: white; padding: 20px; text-decoration: none; border-radius: 10px; font-weight: bold;">
            ✅ GO TO MIRROR
        </a>
    </body>
    </html>
    """

def main():
    if not os.path.exists(REPO_NAME): os.makedirs(REPO_NAME)
    os.chdir(REPO_NAME)

    # 1. Генерируем страницы
    print("[*] Создаем HTML-страницы...")
    for key in KEYWORDS:
        fname = key.replace(" ", "-") + ".html"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(generate_html(key))

    # Создаем главную index.html (карта сайта)
    with open("index.html", "w", encoding="utf-8") as f:
        links = "".join([f'<li><a href="{k.replace(" ", "-")}.html">{k}</a></li>' for k in KEYWORDS])
        f.write(f"<h1>Site Map</h1><ul>{links}</ul>")

    # 2. Магия Git (Заливка на GitHub)
    print("[*] Пушим файлы в облако...")
    commands = [
        "git init",
        "git add .",
        'git commit -m "Initial doorway deployment"',
        "git branch -M main",
        f"git remote add origin https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO_NAME}.git",
        "git push -u origin main --force"
    ]
    
    for cmd in commands:
        subprocess.run(cmd, shell=True)

    print(f"\n[DONE] Проверь репозиторий: https://github.com/{GITHUB_USER}/{REPO_NAME}")

if __name__ == "__main__":
    main()
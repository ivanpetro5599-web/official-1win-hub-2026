import os

# --- НАСТРОЙКИ ---
# Укажи название папки, где лежат твои 11000 html файлов
# Если они лежат в той же папке, где этот скрипт, поставь точку "."
PAGES_DIR = "." 

# Имя выходного файла
OUTPUT_FILE = "index.html"

# Базовая ссылка на твой сайт (чтобы ссылки были полными, это лучше для SEO)
BASE_URL = "https://ivanpetro5599-web.github.io/official-1win-hub-2026/"

def create_mega_index():
    print("[*] Начинаем сканирование файлов...")
    
    # Собираем все .html файлы, кроме самого index.html
    files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html') and f != OUTPUT_FILE]
    files.sort() # Сортируем по алфавиту
    
    print(f"[*] Найдено {len(files)} страниц. Генерируем Хаб...")

    # Начало HTML файла
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OFFICIAL 1WIN HUB 2026 - FULL SITEMAP</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #121212; color: #fff; padding: 20px; }}
            h1 {{ color: #FFD700; text-align: center; }}
            .link-container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 10px; }}
            a {{ text-decoration: none; color: #4da6ff; background: #1e1e1e; padding: 10px; border-radius: 5px; display: block; }}
            a:hover {{ background: #333; color: #FFD700; }}
        </style>
    </head>
    <body>
        <h1>🚀 1WIN OFFICIAL MIRRORS & BONUSES 2026 ({len(files)} PAGES)</h1>
        <p style="text-align:center;">Updates daily. Verified links.</p>
        <div class="link-container">
    """

    # Добавляем ссылки
    for filename in files:
        # Убираем .html и дефисы для красивого названия ссылки
        clean_name = filename.replace("-", " ").replace(".html", "").title()
        full_link = BASE_URL + filename
        
        # Добавляем блок ссылки
        html_content += f'<a href="{filename}">{clean_name}</a>\n'

    # Конец HTML файла
    html_content += """
        </div>
    </body>
    </html>
    """

    # Запись файла
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[✅] ГОТОВО! Файл {OUTPUT_FILE} создан.")
    print(f"Теперь загрузи его в корень репозитория на GitHub (перетащи мышкой).")

if __name__ == "__main__":
    create_mega_index()
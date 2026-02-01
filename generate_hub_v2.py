import os
import sys

# --- НАСТРОЙКИ ---
PAGES_DIR = "."  # Ищем файлы прямо тут
OUTPUT_FILE = "index.html"
BASE_URL = "https://ivanpetro5599-web.github.io/official-1win-hub-2026/"

def create_mega_index():
    # Получаем реальный путь, где лежит скрипт
    current_folder = os.getcwd()
    print(f"[*] Скрипт запущен в папке:\n    {current_folder}")
    print("[*] Ищу .html файлы...")
    
    # Собираем файлы
    files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html') and f != OUTPUT_FILE]
    files.sort()
    
    count = len(files)
    
    # === ГЛАВНАЯ ПРОВЕРКА ===
    if count == 0:
        print("\n" + "="*50)
        print("[❌] ОШИБКА! Я НЕ ВИЖУ HTML ФАЙЛОВ!")
        print("="*50)
        print("Брат, ты положил скрипт не туда.")
        print("Положи этот файл ПРЯМО ВНУТРЬ папки с твоими 11000 страницами.")
        input("\nНажми Enter, чтобы выйти...")
        return

    print(f"\n[✅] НАЙДЕНО: {count} страниц. Генерирую index.html...")

    # Генерация HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>OFFICIAL 1WIN HUB 2026 - {count} MIRRORS</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #0f0f0f; color: #e0e0e0; margin: 0; padding: 20px; }}
            h1 {{ color: #FFD700; text-align: center; font-size: 24px; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 2px; }}
            p.stats {{ text-align: center; color: #888; margin-bottom: 30px; font-size: 14px; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; max-width: 1200px; margin: 0 auto; }}
            a {{ display: block; text-decoration: none; color: #fff; background: #1f1f1f; padding: 15px; border-radius: 8px; font-size: 14px; border: 1px solid #333; transition: 0.2s; }}
            a:hover {{ border-color: #FFD700; background: #2a2a2a; transform: translateY(-2px); }}
            span.icon {{ color: #FFD700; margin-right: 8px; }}
        </style>
    </head>
    <body>
        <h1>🚀 1WIN OFFICIAL MIRRORS 2026</h1>
        <p class="stats">Updated: Just Now • Total Links: {count}</p>
        <div class="grid">
    """

    for filename in files:
        clean_name = filename.replace("-", " ").replace(".html", "").title()
        # Если имя слишком длинное, обрезаем
        if len(clean_name) > 30: clean_name = clean_name[:27] + "..."
        
        html_content += f'<a href="{filename}"><span class="icon">⚡</span>{clean_name}</a>\n'

    html_content += """
        </div>
    </body>
    </html>
    """

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"\n[✅] ПОБЕДА! Файл {OUTPUT_FILE} создан.")
    print(f"Размер файла: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB")
    print("Теперь залей его на GitHub!")
    input("\nНажми Enter, чтобы выйти...")

if __name__ == "__main__":
    create_mega_index()
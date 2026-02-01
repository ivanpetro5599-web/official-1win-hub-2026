import os
import datetime

# --- НАСТРОЙКИ ---
PAGES_DIR = "." 
INDEX_FILE = "index.html"
SITEMAP_FILE = "sitemap.xml"
BASE_URL = "https://ivanpetro5599-web.github.io/official-1win-hub-2026/"

def create_hub_and_sitemap():
    print(f"[*] Скрипт запущен. Ищу файлы...")
    
    # Собираем файлы
    files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html') and f != INDEX_FILE]
    files.sort()
    
    count = len(files)
    if count == 0:
        print("[❌] ОШИБКА: Нет HTML файлов в этой папке!")
        input("Нажми Enter..."); return

    print(f"[✅] Найдено {count} страниц.")

    # --- ЧАСТЬ 1: ГЕНЕРАЦИЯ INDEX.HTML (Для людей) ---
    print("[1/2] Генерирую index.html...")
    html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OFFICIAL 1WIN MIRRORS - {count} LINKS</title>
    <style>
        body {{ font-family: sans-serif; background: #111; color: #fff; padding: 20px; }}
        a {{ display: block; color: #4da6ff; text-decoration: none; padding: 5px; }}
        a:hover {{ color: #FFD700; }}
    </style>
</head>
<body>
    <h1>VERIFIED MIRRORS 2026 ({count})</h1>
    <div class="list">
"""
    for f in files:
        html_content += f'<a href="{f}">{f.replace(".html", "")}</a>\n'
    
    html_content += "</div></body></html>"
    
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    # --- ЧАСТЬ 2: ГЕНЕРАЦИЯ SITEMAP.XML (Для Гугла) ---
    print("[2/2] Генерирую sitemap.xml...")
    
    # Дата сегодня в формате YYYY-MM-DD
    today = datetime.date.today().isoformat()
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Добавляем главную страницу
    xml_content += f'  <url>\n    <loc>{BASE_URL}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n'
    
    # Добавляем все остальные страницы
    for f in files:
        full_url = BASE_URL + f
        xml_content += f'  <url>\n    <loc>{full_url}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n'
        
    xml_content += '</urlset>'

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f"\n[🔥] ГОТОВО! Созданы два файла:\n1. {INDEX_FILE}\n2. {SITEMAP_FILE}")
    print("Залей ОБА файла на GitHub!")
    input("Нажми Enter чтобы выйти...")

if __name__ == "__main__":
    create_hub_and_sitemap()
import os
import random
import shutil

# --- НАСТРОЙКИ ---
BASE_DOMAIN = "https://ivanpetro5599-web.github.io/official-1win-hub-2026"
OUTPUT_DIR = "dist"
TOTAL_PAGES = 1000  # Сколько страниц делать

# Словари для генерации бредо-текста (чтобы Google думал, что это уникально)
TITLES = ["Official Mirror", "Fast Login", "Secure Entry", "Mobile App", "Bonus 2026", "Betting Site"]
TEXTS = [
    "Access the platform instantly through our verified hub.",
    "Do not trust fake links, use only official mirrors updated daily.",
    "Big bonuses are waiting for new players who register now.",
    "Sports betting and casino games are available 24/7 via this link.",
    "Bypass blocks safely and securely with our new method."
]

def generate_factory():
    # 1. Очистка старой папки
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    print(f"[🧹] Папка {OUTPUT_DIR} очищена.")

    print(f"[⚙️] Начинаю штамповать {TOTAL_PAGES} страниц...")

    # Создаем список имен файлов заранее для перелинковки
    filenames = [f"page-{i}.html" for i in range(1, TOTAL_PAGES + 1)]

    for i, filename in enumerate(filenames):
        # Генерируем уникальный контент
        title = f"1Win {random.choice(TITLES)} #{i+1}"
        desc = f"{random.choice(TEXTS)} {random.choice(TEXTS)}"
        
        # Перелинковка: ссылка на следующую и 3 случайные
        random_links = random.sample(filenames, 3)
        links_html = "<ul>"
        for link in random_links:
            links_html += f'<li><a href="{link}">See also: {link.replace(".html", "")}</a></li>'
        links_html += "</ul>"

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <meta name="description" content="{desc}">
            <meta charset="UTF-8">
        </head>
        <body>
            <h1>{title}</h1>
            <p>{desc}</p>
            <p><strong>Status:</strong> Online ✅</p>
            <div style="padding: 20px; background: #eee;">
                <a href="ТВОЯ_ПАРТНЕРСКАЯ_ССЫЛКА" style="color: red; font-size: 20px;">[ CLICK TO PLAY ]</a>
            </div>
            <hr>
            <h3>Related Pages:</h3>
            {links_html}
            <small>Updated: 2026-02-01 | ID: {random.randint(10000,99999)}</small>
        </body>
        </html>
        """
        
        with open(f"{OUTPUT_DIR}/{filename}", "w", encoding="utf-8") as f:
            f.write(html)
            
    print(f"[✅] ГОТОВО! Создано {TOTAL_PAGES} страниц в папке {OUTPUT_DIR}.")

if __name__ == "__main__":
    generate_factory()
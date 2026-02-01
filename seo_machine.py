import os
import random

# --- НАСТРОЙКИ ---
KEYWORDS = ["1win mirror 2026", "official 1win login", "1win sports betting", "1win promo code today"] # Сюда грузи свои 1000 ключей
BASE_DOMAIN = "https://ivanpetro5599-web.github.io/official-1win-hub-2026"

def generate_seo_farm():
    if not os.path.exists("dist"): os.makedirs("dist")
    
    # Сначала создаем список всех будущих имен файлов
    all_files = [k.replace(" ", "-").lower() + ".html" for k in KEYWORDS]

    for i, key in enumerate(KEYWORDS):
        current_file = all_files[i]
        
        # Генерируем блок перелинковки (5 случайных ссылок из нашего же списка)
        other_files = [f for f in all_files if f != current_file]
        random_links = random.sample(other_files, min(5, len(other_files)))
        linking_html = "<h3>Related Topics:</h3><ul>"
        for link in random_links:
            linking_html += f'<li><a href="{link}">{link.replace("-", " ").replace(".html", "")}</a></li>'
        linking_html += "</ul>"

        # Шаблон страницы
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{key.upper()} | Official Mirror 2026</title>
            <meta name="description" content="Access {key} safely. Secure links for 2026.">
        </head>
        <body>
            <h1>{key} - Working Link</h1>
            <p>Looking for {key}? Our portal provides the most stable access to the platform in 2026. 
               Avoid phishing and use only verified sources.</p>
            
            <div style="background: #f0f0f0; padding: 20px; text-align: center;">
                <a href="ТВОЯ_ПАРТНЕРКА" style="font-size: 24px; color: red; font-weight: bold;">➡️ CLICK TO LOGIN / REGISTER ⬅️</a>
            </div>

            <hr>
            {linking_html}
        </body>
        </html>
        """

        with open(f"dist/{current_file}", "w", encoding="utf-8") as f:
            f.write(html_content)
        
    print(f"[✅] Сгенерировано {len(KEYWORDS)} уникальных страниц с перелинковкой.")

if __name__ == "__main__":
    generate_seo_farm()
import os

# --- НАСТРОЙКИ ---
# Убедись, что путь к папке совпадает с реальностью!
DOMAIN = "https://ivanpetro5599-web.github.io/official-1win-hub-2026"
FOLDER_NAME = "official-1win-hub-2026"

def create_sitemap():
    # Проверяем, существует ли папка
    if not os.path.exists(FOLDER_NAME):
        print(f"[!] Ошибка: Папка {FOLDER_NAME} не найдена!")
        return

    # Собираем все HTML файлы
    files = [f for f in os.listdir(FOLDER_NAME) if f.endswith('.html')]
    print(f"[*] Найдено {len(files)} страниц. Генерируем карту...")

    sitemap_path = os.path.join(FOLDER_NAME, "sitemap.xml")
    
    with open(sitemap_path, "w", encoding="utf-8") as s:
        s.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        s.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        
        for f in files:
            # Превращаем имя файла в URL
            s.write(f'  <url><loc>{DOMAIN}/{f}</loc></url>\n')
            
        s.write('</urlset>')
    
    print(f"[УСПЕХ] Файл создан: {sitemap_path}")

if __name__ == "__main__":
    create_sitemap()
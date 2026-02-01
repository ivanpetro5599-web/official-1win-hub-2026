import os

def fix_github_404():
    print("--- ЛЕЧЕНИЕ ОШИБКИ 404 ---")
    
    # 1. Создаем файл-блокировщик Jekyll (это главная причина ошибок)
    with open(".nojekyll", "w") as f:
        f.write("")
    print("[✅] Файл .nojekyll создан.")

    # 2. Создаем главную страницу (чтобы корень не был пустым)
    html = """<h1>OFFICIAL HUB IS ONLINE</h1><a href='page-1.html'>Enter Site</a>"""
    with open("index.html", "w") as f:
        f.write(html)
    print("[✅] Index.html восстановлен.")

    # 3. Отправляем это на сервер
    print("[🚀] Отправка исправлений...")
    os.system("git add .")
    os.system('git commit -m "Fix 404: Add nojekyll"')
    os.system("git push")
    print("--- ГОТОВО! Жди 2 минуты и проверяй ссылку снова ---")

if __name__ == "__main__":
    fix_github_404()
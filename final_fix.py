import os
import shutil
import time

def force_push_fix():
    print("--- 🔨 ФИНАЛЬНЫЙ РЕМОНТ ---")

    # 1. Удаляем папку-паразита (вложенный репозиторий), которая путает Гит
    parasite_folder = "official-1win-hub-2026"
    if os.path.exists(parasite_folder) and os.path.isdir(parasite_folder):
        print(f"[🧹] Удаляю лишнюю папку '{parasite_folder}'...")
        # Используем команду системы, она надежнее для скрытых папок
        os.system(f'rmdir /S /Q "{parasite_folder}"')
    
    # 2. Гарантируем наличие .nojekyll
    with open(".nojekyll", "w") as f:
        f.write("")
    print("[✅] .nojekyll на месте.")

    # 3. Меняем Index.html (добавляем время), чтобы Гит УВИДЕЛ изменения
    current_time = time.strftime("%H:%M:%S")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>OFFICIAL SITE</title></head>
    <body>
        <h1>SITE IS LIVE ✅</h1>
        <p>Last Update: {current_time}</p>
        <hr>
        <a href="page-1.html" style="font-size:20px; color:red;">>>> ENTER HERE <<<</a>
    </body>
    </html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[✅] Index.html обновлен (Время: {current_time}).")

    # 4. Отправляем
    print("--- ОТПРАВКА НА GITHUB ---")
    os.system("git add .")
    os.system('git commit -m "Final Fix: Remove submodule and update index"')
    push_code = os.system("git push")

    if push_code == 0:
        print("-" * 30)
        print("[🎉] УСПЕХ! Изменения улетели.")
        print("Жди 1-2 минуты и открывай сайт.")
    else:
        print("[❌] Ошибка пуша.")

if __name__ == "__main__":
    force_push_fix()
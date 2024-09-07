import webbrowser
import os

# URL сайта, который нужно открыть
url = "https://www.youtube.com"

# Функция для открытия сайта в браузере по умолчанию
def open_site():
    webbrowser.open(url, new=2)

# Запуск функции
if __name__ == "__main__":
    open_site()

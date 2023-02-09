"""
СОРТИРОВКА ЗАГРУЗОК

работа с файлами в директории

Возможно Вам знакома проблема, когда в папке с загрузками много всякого разного и очень сложно найти то,
что действительно нужно.
Мы попробуем решить эту проблему. Создадим сортировщик, который раскидает все наши файлы по разным папкам
в зависимости от расширения файлов.
"""

import os

# получение имени пользователя
# USERNAME is for Windows, USER is for Linux
username = os.environ.get('USER', os.environ.get('USERNAME'))

# получение пути к сортируемой директории
path_to_download_windows = os.path.join("c:\\", "Users", username, "Downloads")  # путь к файлу загрузок в windows
path_to_download_linux = os.path.join("home", username, "Downloads")  # path in linux
path_to_download = path_to_download_windows if os.name == "nt" else path_to_download_linux

# создаём правила для сортировки, можно добавить что-то дополнительно
extension_parser = {
    "music": ["mp3", "m4a", "wav"],
    "video": ["mp4", "avi"],
    "image": ["jpg", "jpeg", "png", "gif", "bmp"],
    "text": ["txt", "doc", "docx", "pdf", "xls", "xlsx", "ppt", "pptx"],
    "archive": ["zip", "rar", "gz", "bz2", "7z"],
    "programs": ["exe", "sh", "bat", "cmd", "ps1", "ps2"],
    "python": ["py", "pyc", "pyo", "pyd", "pyw"],
    "other": [],
}

# создаём папки под каждый тип файлов
for extension in extension_parser.keys():
    extension_path = os.path.join(path_to_download, extension)
    if not os.path.exists(extension_path):
        os.mkdir(extension_path)

# пробегаемся по содержимому загрузок
# отбираем только файлы, перекидываем их в соответствующие папки
for i in os.listdir(path_to_download):
    old_path = os.path.join(path_to_download, i)
    # проверяем что это файл, а не папка
    if os.path.isfile(old_path):
        # ищем подходящую папку
        new_folder = "other"
        for extension in extension_parser.keys():
            if i.rsplit(".", 1)[1] in extension_parser[extension]:
                new_folder = extension
                break
        new_path = os.path.join(path_to_download, new_folder, i)
        os.rename(old_path, new_path)
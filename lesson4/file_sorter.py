import os


path_to_download = os.path.join("c:\\", "Users", "user", "Downloads")
# path_to_download = os.path.join("home", "USERNAME", "Downloads")
# whoami

extension_parser = {
    "music": [".mp3", ".m4a"],
    "video": [".mp4", ".avi"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "text": [".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "archive": [".zip", ".rar", ".gz", ".bz2", ".7z"],
    "other": [],
}


for i in os.listdir(path_to_download):
    print(i.rsplit(".", 1))
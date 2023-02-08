import os


path_to_download = os.path.join("c:\\", "Users", "user", "Downloads")



for i in os.listdir(path_to_download):
    print(i)
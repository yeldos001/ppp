#Напишите программу на Python, чтобы проверить, существует ли данный путь или нет. Если путь существует, найдите имя файла и часть каталога указанного пути.
import os

def split_path(path):
    if os.path.exists(path):
        return os.path.split(path)
    return None

print(split_path("/home/user/file.txt"))
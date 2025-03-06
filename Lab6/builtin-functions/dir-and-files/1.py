#Напишите программу на Python, чтобы перечислять только директории, файлы и все директории, файлы по указанному пути.
import os

def list_files_and_dirs(path="."):
    return os.listdir(path)

print(list_files_and_dirs())
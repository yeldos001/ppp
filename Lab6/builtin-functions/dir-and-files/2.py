#Напишите программу на Python для проверки доступа к указанному пути. Проверка наличия, удобочитаемости, записываемости и исполняемости указанного пути
import os

def check_path_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

print(check_path_access("test.txt"))
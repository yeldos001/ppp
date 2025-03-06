#Напишите программу на Python для создания 26 текстовых файлов с именами A.txt, B.txt и так далее до Z.txt
import string

def create_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as f:
            f.write(f"This is file {letter}.txt")

create_files()
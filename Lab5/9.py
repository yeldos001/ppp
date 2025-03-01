#Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.
import re

text = "HelloWorldPython"

result = re.sub(r"(?=[A-Z])", " ", text).strip()
print(result)
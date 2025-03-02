#Напишите программу на Python для разделения строки на прописные буквы.
import re

text = "HelloWorldPython"

result = re.split(r"(?=[A-Z])", text)
print(result)
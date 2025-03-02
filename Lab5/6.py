#Напишите программу на Python для замены всех вхождений пробела, запятой или точки на двоеточие.
import re

text = "Hello, world. How are you?"

result = re.sub(r"[ ,.]", ":", text)
print(result)
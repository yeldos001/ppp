#Напишите программу на Python, которая соответствует строке, за которой следует что угодно, оканчивающаяся на .'a''b'
import re

pattern = r"a.*b$"

test_strings = [
    "acb",
    "a123b",
    "abc",
    "a",
    "b",
    "abx",
]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")
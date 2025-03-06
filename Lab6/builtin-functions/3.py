#Напишите программу на Python со встроенной функцией, которая проверяет, является ли переданная строка палиндромом или нет.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    for i in range(a, b + 1):  # Перебираем числа от a до b
        yield i ** 2  # Возвращаем квадрат числа

# Ввод диапазона
a = int(input("Введите начало диапазона (a): "))
b = int(input("Введите конец диапазона (b): "))

# Тестирование генератора
for square in squares(a, b):
    print(square)

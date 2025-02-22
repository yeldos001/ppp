#Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n  # Возвращаем текущее число
        n -= 1   # Уменьшаем n на 1

# Ввод числа n
n = int(input("Введите число n: "))

# Используем генератор и выводим числа
for num in countdown(n):
    print(num)

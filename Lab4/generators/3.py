#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):  # Перебираем числа от 0 до n
        if i % 3 == 0 and i % 4 == 0:  # Проверяем делимость на 3 и 4
            yield i  # Возвращаем число

# Ввод числа n
n = int(input("Введите число n: "))

# Используем генератор и выводим числа
print(list(divisible_by_3_and_4(n)))

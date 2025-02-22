#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(0, n + 1, 2):  # Перебираем только чётные числа
        yield str(i)  # Возвращаем строку для удобства объединения

# Ввод числа n
n = int(input("Введите число n: "))

# Используем генератор и выводим результат
print(",".join(even_numbers(n)))

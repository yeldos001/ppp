#Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2  # Генерируем квадрат числа

# Пример использования
N = 10
for square in square_generator(N):
    print(square)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 17, 18, 19, 20]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(f"Prime numbers: {prime_numbers}")
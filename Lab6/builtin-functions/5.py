#Напишите программу на Python со встроенной функцией, которая возвращает True, если все элементы кортежа истинны.
def all_true(elements):
    return all(elements)

print(all_true((True, True, False))) 
print(all_true((True, True, True)))
#Напишите программу на Python, которая вызывает функцию квадратного корня через определенные миллисекунды
import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000) 
    return math.sqrt(number)

print(delayed_sqrt(25100, 2123))
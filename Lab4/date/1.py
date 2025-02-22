#Write a Python program to subtract five days from current date
from datetime import datetime, timedelta

# Получаем текущую дату
current_date = datetime.now()

# Вычитаем 5 дней
new_date = current_date - timedelta(days=5)

# Выводим результат
print("Текущая дата:", current_date.strftime("%Y-%m-%d"))
print("Дата минус 5 дней:", new_date.strftime("%Y-%m-%d"))

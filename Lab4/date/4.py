#Write a Python program to calculate two date difference in seconds.
from datetime import datetime

# Задаем две даты
date1 = datetime(2025, 2, 20, 12, 0, 0)  # 20 февраля 2025 года, 12:00:00
date2 = datetime(2025, 2, 22, 14, 30, 0)  # 22 февраля 2025 года, 14:30:00

# Вычисляем разницу в секундах
difference = abs((date2 - date1).total_seconds())

# Выводим результат
print("Разница в секундах:", difference)

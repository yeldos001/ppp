# Write a Python program to drop microseconds from datetime.
from datetime import datetime

# Получаем текущее дату и время
current_datetime = datetime.now()

# Убираем микросекунды
new_datetime = current_datetime.replace(microsecond=0)

# Выводим результат
print("До удаления микросекунд:", current_datetime)
print("После удаления микросекунд:", new_datetime)

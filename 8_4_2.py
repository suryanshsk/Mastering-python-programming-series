from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

today = datetime.today()
print("Today's date:", today)

formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted_date)

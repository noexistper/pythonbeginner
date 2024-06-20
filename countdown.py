import time
import datetime
import os
os.system("cls")
number = input("Enter time in seconds::")
number = int(number)
print(f"Starting countdown for {number} seconds.")
hours = str(datetime.timedelta(seconds=number))
print(f"{hours}")
time.sleep(1)
os.system("cls")
for i in range(number):
    number -= 1
    time.sleep(1)
    os.system("cls")
    if number == 0:
        print(f"Time Ended")
    else:
        hours = str(datetime.timedelta(seconds=number))
        print(hours)

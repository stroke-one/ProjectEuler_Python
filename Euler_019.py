import time
import calendar

t = time.time()

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if calendar.weekday(year, month, 1) == 6:
            count += 1

print("First of month Mondays: ", count)

print(time.time() - t)





































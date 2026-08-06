###Create a python program capable of greeting you with GOOD MORINING , GOOD AFTERNOON and GOOD EVENING
#YOUR program should use the time module to determine the current hour

import time
timestamp_main = (time.strftime("%H:%M:%S"))
print(timestamp_main)
timestamp_H = time.strftime("%H")
print(timestamp_H)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)

if int(timestamp_H) < 12:
    print("Good Morining")
elif int(timestamp_H) >= 12 and int(timestamp_H) < 18:
    print("Good Afternoon")
elif int(timestamp_H) >= 18 and int(timestamp_H) < 20:
    print("Good Evening")
else:
    print("Good Night")


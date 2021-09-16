number = 0
am = 0
pm = 0

while number <= 24 and number >= 0:
    if number < 12:
        am = am + 1
        print(str(am) + ":00 AM")
    elif number > 12:
        pm = pm + 1
        print(str(pm) + ":00 PM")
    number = number + 1
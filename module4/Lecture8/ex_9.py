d = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}

while True:
    try:
        day = int(input('Enter the day number: '))
    except ValueError:
        print('Please type a number')
    else:
        print(d.get(day, 'There are no such day!'))
from datetime import datetime


if __name__ == '__main__':
    d1 = datetime(year=2012, month=1, day=7, hour=14)
    print(d1)

    days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }

    seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
    print(days[seventh_day_2020.weekday()])

    curr_day = datetime.now()
    print(days[curr_day.weekday()])

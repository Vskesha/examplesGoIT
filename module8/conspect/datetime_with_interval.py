from datetime import datetime, timedelta


if __name__ == '__main__':
    seventh_day_2020 = datetime(2020, 1, 7)
    four_weeks_interval = timedelta(weeks=4)

    print(seventh_day_2020 + four_weeks_interval)
    print(seventh_day_2020 - four_weeks_interval)

    now = datetime.now()
    delta = timedelta(weeks=1)

    print(now + delta)
    print(now - delta)

    print(now.weekday())
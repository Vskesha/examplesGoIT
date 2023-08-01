from datetime import datetime


if __name__ == '__main__':

    seventh_day_2019 = datetime(2019, 1, 7)
    seventh_day_2020 = datetime(2020, 1, 7)

    diff = seventh_day_2020 - seventh_day_2019
    print(diff)
    print(diff.total_seconds())
    print(diff.days)
from datetime import datetime


if __name__ == '__main__':
    current_datetime = datetime.now()
    future_month = current_datetime.month % 12 + 1
    future_year = current_datetime.year + current_datetime.month // 12
    future_datetime = datetime(future_year, future_month, 1)

    print(future_datetime)
    print(current_datetime < future_datetime)
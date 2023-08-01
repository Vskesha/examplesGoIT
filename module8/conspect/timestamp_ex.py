from datetime import datetime


if __name__ == '__main__':
    seventh_day_2020 = datetime(2020, 1, 7, 14)
    ts = seventh_day_2020.timestamp()
    print(ts)
    print(type(ts))
    ts += 100_000
    print(datetime.fromtimestamp(ts))
    

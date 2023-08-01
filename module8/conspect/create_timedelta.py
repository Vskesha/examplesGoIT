from datetime import timedelta, datetime


if __name__ == '__main__':
    delta = timedelta(days=50,
                      seconds=27,
                      microseconds=10,
                      milliseconds=29000,
                      minutes=5,
                      hours=8,
                      weeks=2)

    now = datetime.now()
    print(now)
    print(now + delta)

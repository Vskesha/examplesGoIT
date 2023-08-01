from datetime import datetime


if __name__ == '__main__':
    seventh_day_2020 = datetime(2020, 1, 7, 14)
    print(seventh_day_2020.strftime('%A %d %B %Y'))

    print(datetime.strptime('10 January 2020', '%d %B %Y'))
    my_date = datetime.strptime('31/01/22 23:59:59.999999',
                                '%d/%m/%y %H:%M:%S.%f')
    print(my_date)

    print(my_date.strftime('%a %d %b %Y, %I:%M%p'))

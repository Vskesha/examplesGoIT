from datetime import datetime


def get_days():
    """Counts the amount or days to the given date"""
    user_input = input("Enter the date in form 'dd.mm': ")
    user_date = datetime.strptime(user_input, '%d.%m')
    now = datetime.now()
    user_date = user_date.replace(year=now.year)
    if now > user_date:
        user_date = user_date.replace(year=now.year + 1)
    delta = user_date - now
    print(f'Remains {delta.days} days to {user_input}')


def make_backup(data):
    curr_time = datetime.now()
    with open(f'backup_{curr_time.timestamp()}.txt', 'w') as fh:
        fh.write(data)


if __name__ == '__main__':
    # get_days()
    data = 'fdklsa hfsdioflf vnoif'
    make_backup(data)

from datetime import datetime, timedelta
import random


def get_random_birthdays(n):
    """Get the list of random birthdays"""
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365 * 80)
    birthdays_list = []
    while len(birthdays_list) < n:
        fake_year = random.randrange(oldest_date.year, current_date.year)
        fake_month = random.randint(1, 12)
        fake_day = random.randint(1, 31)
        try:
            fake_birthday = datetime(fake_year, fake_month, fake_day)
        except ValueError:
            continue
        if current_date >= fake_birthday:
            birthdays_list.append(fake_birthday)

    return birthdays_list


if __name__ == '__main__':
    birthday_list = get_random_birthdays(10)
    print(random.sample(birthday_list, k=3))

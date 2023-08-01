def get_number(x):
    numbers = []
    for i in range(x):
        num = i ** 2
        if not num % 2:
            numbers.append(num)
    print(numbers)


def get_numbers_short(x):
    numbers = {i: i ** 2 for i in range(x) if not i % 2}
    print(numbers)
    print(type(numbers))


if __name__ == '__main__':
    get_number(20)
    get_numbers_short(20)

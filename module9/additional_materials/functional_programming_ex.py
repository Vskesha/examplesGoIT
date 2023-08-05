import math


def get_length(d):
    result = d * math.pi
    return result


get_length_lambda = lambda d: d * math.pi


def get_remainder(data):
    result = []
    for n in data:
        rem = n % 2
        result.append(rem)
    return result


def check_num(data):
    result = []
    for n in data:
        rem = n % 2
        if not rem:
            result.append(n)
    return result


if __name__ == '__main__':
    # len1 = get_length(10)
    # len2 = get_length_lambda(10)
    # print(len1, len2, sep='\n')

    data = [1, 2, 3, 4, 5, 6]
    # print(*get_remainder(data))
    # print(*map(lambda n: n % 2, data))

    check_data = check_num(data)
    print(*check_data)
    check_data_filter = filter(lambda x: not x % 2, data)
    print(*check_data_filter)
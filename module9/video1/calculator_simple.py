def operate(x, y, operator):
    return OPERATIONS.get(operator, nope)(x, y)


def nope(x, y):
    print('There is no such operation')


def summ(x, y):
    return x + y


def mul(x, y):
    return x * y


def subtract(x, y):
    return x - y


def division(x, y):
    return x / y


def pow(x, y):
    return x ** y


OPERATIONS = {
    '-': subtract,
    '+': summ,
    '*': mul,
    '/': division,
    '**': pow,
}


if __name__ == '__main__':
    while True:
        x = int(input('X: '))
        y = int(input('Y: '))
        operator = input('Operator: ')
        print(operate(x, y, operator))

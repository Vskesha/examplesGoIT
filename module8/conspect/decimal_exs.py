from decimal import Decimal, getcontext


if __name__ == '__main__':
    getcontext().prec = 6
    print(Decimal(1) / Decimal(7))
    getcontext().prec = 28
    print(Decimal(1) / Decimal(7))
    print(0.1 + 0.2 == 0.3)
    print(0.1 + 0.2)

def my_range(x, y):

    while x < y:
        yield x
        x += 1


if __name__ == '__main__':
    for i in my_range(0, 10):
        print(i)

    a = (i for i in [1, 2, 3])
    print(a)
def func(n):
    i = 0
    while i < n:
        print('Entry point')
        yield f'Point to yield {i + 1}'
        print('After yield')
        i += 1


if __name__ == '__main__':
    generator = func(3)
    for element in generator:
        print(element)

def outer(x):
    def inner(y):
        print(f'{x} + {y} = {x + y}')
    return inner


def get_cache(cache=None):
    cache = cache or {}
    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum(i for i in range(1, n + 1))
            print(f'Hard work: {n}')
        else:
            print('Easy work')
        return cache[n]
    return inner


def main():
    data = {5: 15, 10: 55, 15: 120}
    calc = get_cache(data)
    print(calc(5))
    print(calc(5))
    print(calc(10))
    print(calc(10))
    print(calc(15))
    print(calc(5))


if __name__ == '__main__':
    main()

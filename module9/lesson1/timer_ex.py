from time import sleep, perf_counter
# from functools import wraps


def time_counter(func):  # decorator
    # @wraps
    def interval(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        passed = perf_counter() - start
        return result, passed
    return interval


# @time_counter
# def test_func(a, b):
#     sleep(a)
#     return a + b


@time_counter
def factorial_with_cache(n, cache=None):

    cache = cache or {}

    if n < 0:
        raise ValueError('Number cannot be negative')

    def calc(n):
        result = 1
        for val in range(1, n + 1):
            if val in cache:
                result = cache[val]
                print(f'{val} in cache {result}')
            else:
                result = val * cache.get(val - 1, 1)
                cache[val] = result
                print(f'{val} not in cache {result}')
        return result
    return calc(n)


if __name__ == '__main__':
    # print(test_func(2, 3))

    f3 = factorial_with_cache(10)
    print(f3[0])
    print(f3[1])

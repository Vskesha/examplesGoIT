import time


def args_logger(func):
    def wrapper(*args):
        if Debug:
            print(f'I am args_logger. Args: {args}')
        result = func(*args)
        return result
    return wrapper


def result_logger(func):
    def wrapper(*args):
        result = func(*args)
        if Debug:
            print(f'I am result_logger. Result: {result}')
        return result
    return wrapper


def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        stop = time.perf_counter()
        if Debug:
            print(f'I am timer. Run time: {stop - start}')
        return result
    return wrapper


@timer
@result_logger
@args_logger
def calc(x, y):
    result = x + y
    return result


Debug = True
# logger = args_logger(calc)


if __name__ == '__main__':
    z = calc(5, 8)
    print(z)
    # print(logger(7, 9))
    print(calc(5, 9))

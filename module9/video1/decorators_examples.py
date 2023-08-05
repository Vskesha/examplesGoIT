from functools import wraps


def decorator_with_arguments(arg):
    def simple_decorator(func):
        @wraps(func)
        def simple_wrapper(*args, **kwargs):
            print(f'Before {arg}')
            result = func(*args, **kwargs)
            print(f'After {arg}')
            return result
        return simple_wrapper
    return simple_decorator


def simple_decorator_2(func):
    @wraps(func)
    def simple_wrapper(*args, **kwargs):
        print('Before func2')
        result = func(*args, **kwargs)
        print('After func2')
        return result
    return simple_wrapper


@simple_decorator_2
def func():
    print('Hello world!')


@decorator_with_arguments('my argument')
def mult(x, y):
    return x * y


if __name__ == '__main__':
    func()
    print(mult(10, 5))
    print(mult.__name__)
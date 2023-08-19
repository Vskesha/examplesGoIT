def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print('action before wrapped obj')
        result = func(self, *args, **kwargs)
        print('actions after wrapped obj')
        return result
    return wrapper


def class_decorator(cls):
    print('class decorator')
    new_cls = cls
    new_cls.value = 55
    new_cls.description = 'core 16 module 11 lesson 2'
    return new_cls


@class_decorator
class Test:
    name = 'Test Class'

    @method_decorator
    def info(self, user):
        return f"Hello {user}. This is {self.name}"


if __name__ == '__main__':
    t = Test()
    print(t.info('Ivan'))
    print(t.value)
    t.value = 10
    print(t.value)
    print(t.description)
    t.description += " !!!222"
    print(t.description)

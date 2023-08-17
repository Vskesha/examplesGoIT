class Foo:
    def __new__(cls, *args, **kwargs):
        print("Method __new__")
        print(args, kwargs)
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print("Method __init__")
        self.value = value


class Baz(Foo):
    def __init__(self, value):
        super(Baz, self).__init__(value)


if __name__ == '__main__':
    baz = Baz(10)
    foo = Baz(20)

    print(baz.value, foo.value)
    print(baz, foo)
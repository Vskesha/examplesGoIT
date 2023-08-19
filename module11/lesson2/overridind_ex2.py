class Adder:
    def __add__(self, other):
        raise NotImplemented


class ListAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


class DictAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return {**self.value, **other.value}


if __name__ == '__main__':
    # Adder() + Adder()
    la1 = ListAdder([1, 2])
    la2 = ListAdder([3, 4])
    print(la1 + la2)
    da1 = DictAdder({'a': 1, 'b': 2})
    da2 = DictAdder({'c': 3, 'b': 4})
    print(da1 + da2)

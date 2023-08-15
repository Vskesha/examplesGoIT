class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


if __name__ == '__main__':

    two_adder = Adder(2)
    print(two_adder(5))
    print(two_adder(4))

    three_adder = Adder(3)
    print(three_adder(5))
    print(three_adder(4))

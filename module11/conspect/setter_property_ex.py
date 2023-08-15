class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


if __name__ == '__main__':
    p = PositiveNumber()
    p.value = 1
    print(p.value)
    p.value= -1
    p._PositiveNumber__value = -1
    print(p.value)
    
class Test:
    def double(self, x: int):
        print(f'Mul by 2 {self.__class__}')
        return x * 2

    @staticmethod
    def triple(x: int):
        print('Mul by ')
        return x * 3

    @classmethod
    def quad(cls, x: int):
        print('Mul by 4')
        return x * 4


if __name__ == '__main__':
    print("calling through obj")
    obj = Test()
    print(obj.double(4))
    print(obj.triple(4))
    print(obj.quad(4))
    print('calling through class')
    # print(Test.double(4))
    print(Test.triple(4))
    print(Test.quad(4))


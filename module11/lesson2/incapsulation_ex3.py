class A:
    def _protected(self):
        print("It's protected method")

    def __private(self):
        print("It's private method")


if __name__ == '__main__':
    a = A()
    a._protected()

    # a.__private()
    a._A__private()
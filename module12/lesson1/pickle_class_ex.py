from pickle import loads, dumps


class A:
    x = 'some'

    def __init__(self):
        print('new A')
        self.y = 'інша змінна'


if __name__ == '__main__':
    a = A()
    s = dumps(a)
    s_class = dumps(A)

    restored_a = loads(s)
    restored_A = loads(s_class)

    print(a.x, a.y)
    print(restored_a.x, restored_a.y)

    print(a == restored_a)
    print(A == restored_A)
    
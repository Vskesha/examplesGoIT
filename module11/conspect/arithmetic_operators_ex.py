from collections import UserDict


class MyDict(UserDict):
    def __add__(self, other):
        self.data.update(other)
        return self

    def __sub__(self, other):
        for key in other:
            if key in self.data:
                self.data.pop(key)
        return self


if __name__ == '__main__':
    d1 = MyDict({1: 'a', 2: 'b', 3: 'e'})
    d2 = MyDict({3: 'c', 4: 'd'})

    d3 = d1 + d2
    print(d3)

    d1 = MyDict({1: 'a', 2: 'b', 3: 'e'})
    d2 = MyDict({3: 'c', 4: 'd'})

    d4 = d1 - d2
    print(d4)

    d1 = MyDict({1: 'a', 2: 'b', 3: 'e'})
    d2 = MyDict({3: 'c', 4: 'd'})

    d5 = d2 - d1
    print(d5)

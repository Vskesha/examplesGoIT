# iterator
from random import randint


class RandomIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        return randint(self.start, self.end)


if __name__ == '__main__':
    my_random_list = RandomIterator(1, 20, 50)
    print(my_random_list)
    for rand in my_random_list:
        print(rand, end=' ')

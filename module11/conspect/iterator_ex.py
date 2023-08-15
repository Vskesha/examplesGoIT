class Iterable:

    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()


if __name__ == '__main__':
    c = CustomIterator()
    for i in c:
        print(i)
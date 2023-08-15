class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


if __name__ == '__main__':
    a = Point(1, 9)
    print(repr(a))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y


if __name__ == '__main__':
    print(Point(0, 0) == Point(0, 0))  # True
    print(Point(0, 0) != Point(0, 0))  # False
    print(Point(0, 0) < Point(1, 0))  # False
    print(Point(0, 0) > Point(0, 1))  # False
    print(Point(0, 2) >= Point(0, 1))  # True
    print(Point(0, 0) <= Point(0, 0))  # True

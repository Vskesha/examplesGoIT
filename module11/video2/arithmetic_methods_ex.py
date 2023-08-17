class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position({self.x}, {self.y})'

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Position(self.x * value, self.y * value)

    def __div__(self, value):
        return Position(self.x / value, self.y / value)

    def __pow__(self, other):
        pass

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.distance_to_zero() < other.distance_to_zero()

    def __gt__(self, other):
        return self.distance_to_zero() > other.distance_to_zero()

    def __le__(self, other):
        return self.distance_to_zero() <= other.distance_to_zero()

    def __ge__(self, other):
        return self.distance_to_zero() >= other.distance_to_zero()

    def distance_to_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    def __xor__(self, other):
        pass


if __name__ == '__main__':
    char_position = Position(1, 1)
    enemy_position = Position(3, 3)
    

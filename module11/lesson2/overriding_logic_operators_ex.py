class Car:
    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.mark}.{self.model}:{self.year}, {self.color} and price is: {self.price}'

    def __eq__(self, other):
        # print('__eq__')
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


if __name__ == '__main__':
    car_a = Car(2021, 'Ford', 'Fusion', 'Black', 28000)
    car_b = Car(2019, 'Toyota', 'Camry', 'White', 28000)
    print(car_a)
    print(car_b)
    print(car_b == car_a)
    print(car_b != car_a)
    print(car_b < car_a)
    print(car_b > car_a)
    print(car_b <= car_a)
    print(car_b >= car_a)
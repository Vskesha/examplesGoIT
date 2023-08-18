# Methods __repr__ and __str__

class Car:
    store_name = 'GoIT'

    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.store_name}: {self.mark} {self.model}: {self.year}, {self.color}'

    def __repr__(self):
        return f'Car({self.year}, {self.mark}, {self.model}, {self.color})'

    def info(self):
        return self.__str__()


if __name__ == '__main__':
    car = Car(2019, 'Tesla', 'Model X', 'white')
    print(car)
    print(car.info())
    print(repr(car))
    print([car])

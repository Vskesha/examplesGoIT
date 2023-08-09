class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi {self.name}'


if __name__ == '__main__':
    p = Person('Boris', 34)
    print(p.name)
    print(p.age)
    print(p.greeting())
    
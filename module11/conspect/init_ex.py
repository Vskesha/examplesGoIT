class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello! I am {self.name}'


if __name__ == '__main__':
    bill = Human('Bill')
    print(bill.say_hello())
    print(bill.age)

    jill = Human('Jill', 20)
    print(jill.say_hello())
    print(jill.age)

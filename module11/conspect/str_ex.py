class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Hello! I am {self.name}'


if __name__ == '__main__':
    bill = Human('Bill')
    bill_str = str(bill)
    print(bill_str)

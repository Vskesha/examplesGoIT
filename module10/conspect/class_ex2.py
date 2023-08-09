class User:
    name = 'UserName'
    age = 15

    def say_name(self):
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age):
        self.age = age


class Human:
    name = ''

    def hello(self, val):
        if self.name:
            return f'Hello {val}! I am {self.name}.'
        return f'Hello {val}'


if __name__ == '__main__':
    bob = User()
    bob.name = 'Bob'

    bob.say_name()
    bob.set_age(25)
    bob.say_name()

    bill = Human()
    print(bill.hello('John'))
    bill.name = 'Bill'
    print(bill.hello('John'))
    
class User:
    def __init__(self, name, age):
        self.__private_name = None
        self.__private_age = None
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__private_name

    @name.setter
    def name(self, value: str):
        if value.isalpha():
            self.__private_name = value
        else:
            raise Exception('Wrong name')

    @property
    def age(self):
        return self.__private_age

    @age.setter
    def age(self, value: str):
        if int(value) >= 18:
            self.__private_age = int(value)
        else:
            raise Exception('Wrong age')


if __name__ == '__main__':
    user_1 = User('Bill', 20)
    print(user_1.name)
    print(user_1.age)

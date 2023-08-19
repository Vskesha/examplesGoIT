class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None
        self.nickname = nickname
        self.age = age
        self.weight = weight

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Animal should have the nickname")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 50:
            self.__age = age
        else:
            raise ValueError("Animal age is wrong")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError('Animal must have weight')


if __name__ == '__main__':
    dog = Animal('Rex', 3, 5)
    print(dog.nickname, dog.age, dog.weight)
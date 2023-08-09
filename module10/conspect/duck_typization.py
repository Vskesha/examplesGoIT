class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


if __name__ == '__main__':
    r = Recorder()
    cat = Cat()
    dog = Dog()
    strange_animal = Chupakabra()

    r.record_animal(cat)
    r.record_animal(dog)
    r.record_animal(strange_animal)

from collections import namedtuple

if __name__ == '__main__':

    person1 = ('Bob', 30, 'Kyiv')
    print(f'Simple Tuple: name = {person1[0]}, age = {person1[1]}, city = {person1[2]}')

    Person = namedtuple('Person', ['name', 'age', 'city'])
    person2 = Person('Nick', 40, 'Lviv')
    person3 = Person('Olena', 17, 'Odesa')

    print(f'Named Tuple: name = {person2.name}, age = {person2[1]}, city = {person2.city}')
    
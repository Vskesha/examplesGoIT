import random


if __name__ == '__main__':

    print(random.randint(1, 1000))

    print(random.random())

    fruits = ['apple', 'banana', 'orange']
    print(fruits)
    random.shuffle(fruits)
    print(fruits)

    print(random.choice(fruits))

    print(random.choices(fruits, k=4))

    print(random.sample(fruits, k=5, counts=[4, 1, 1]))

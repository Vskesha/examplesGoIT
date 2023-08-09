class User:
    name = 'UserName'
    age = 15


if __name__ == '__main__':
    user1 = User()
    print(user1.name)
    print(user1.age)

    user2 = User()
    user2.name = 'John'
    user2.age = 90

    print(user2.name)
    print(user2.age)

    print(dir(user1))

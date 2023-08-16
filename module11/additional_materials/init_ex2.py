class User:
    # name = None
    # last_name = None
    def __init__(self, name, last_name=None) -> None:
        self.name = name
        self.last_name = last_name

    def get_full_name(self):
        return f'Full name is: {self.name} {self.last_name} (method get_full_name)'

    # def __str__(self):
    #     return f'This is {self.name} {self.last_name} (method __str__)'

    def __repr__(self):
        return f'User({self.name}, {self.last_name})'


if __name__ == '__main__':
    user_1 = User(name='Boris', last_name='Johnson')
    # user_1.name = 'Boris'
    # user_1.last_name = 'Johnson'
    print(user_1.name, user_1.last_name)
    print(user_1)
    # print(get_full_name(user_1))
    print(user_1.get_full_name())

    users = [user_1]
    print(users)

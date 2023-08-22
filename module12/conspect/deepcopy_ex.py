from copy import deepcopy


class Human:
    def __init__(self, name: str, age_weight: list):
        self.name = name
        self.age_weight = age_weight

    def __repr__(self):
        return f'Human({repr(self.name)}, {repr(self.age_weight)})'


if __name__ == '__main__':
    my_list = [1, 2, {1: 'a'}]
    copy_list = deepcopy(my_list)
    copy_list.append(4)
    print(my_list)
    print(copy_list)

    copy_list[2][2] = 'b'
    print(my_list)
    print(copy_list)

    bob = Human('Bob', [35, 80])
    another_bob = deepcopy(bob)
    print(bob, another_bob)
    another_bob.name = 'Bobby'
    print(bob, another_bob)
    another_bob.age_weight[0] = 25
    print(bob, another_bob)
    another_bob.age_weight[1] = 65
    print(bob, another_bob)
    another_bob.age_weight = [10, 40]
    print(bob, another_bob)

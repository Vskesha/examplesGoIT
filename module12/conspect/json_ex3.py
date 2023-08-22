import json


class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Human({repr(self.name)})'


if __name__ == '__main__':

    bob = Human('Bob')
    file_name = 'data2.json'

    with open(file_name, 'w') as fh:
        # json.dump(bob, fh)
        # TypeError: Object of type Human is not JSON serializable
        json.dump(repr(bob), fh)

    with open(file_name, 'r') as fh:
        unpacked = json.load(fh)

    print(unpacked == bob)
    print(unpacked is bob)
    print(unpacked)
    print(type(unpacked))

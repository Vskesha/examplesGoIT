import pickle


class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Human({repr(self.name)})'


if __name__ == '__main__':
    bob = Human('Bob')

    with open('data_bob.bin', 'wb') as fh:
        pickle.dump(bob, fh)

    print(bob)
    print(bob.__dict__)

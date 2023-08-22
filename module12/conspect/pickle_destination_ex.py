import pickle
from pickle_source_ex import Human


if __name__ == '__main__':
    with open('data_bob.bin', 'rb') as fh:
        bob = pickle.load(fh)

    print(bob)

import pickle
from pickle_getstate_ex import MyReader


if __name__ == '__main__':
    with open('savedmyreader.bin', 'rb') as fh:
        my_reader = pickle.load(fh)

    print(my_reader)

    print(my_reader.read(12))
    print(my_reader.read(11))
    print(my_reader.read(15))
    print(my_reader.read(10))
    my_reader.close()
    print('my_reader closed')
    print(my_reader)
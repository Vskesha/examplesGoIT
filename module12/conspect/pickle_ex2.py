import pickle

if __name__ == '__main__':
    some_data = {
        (1, 3, 5): 'tuple',
        2: [1, 2, 3],
        'a': {'key': 'value'}
    }

    file_name = 'data.bin'

    with open(file_name, 'wb') as fh:
        pickle.dump(some_data, fh)

    with open(file_name, 'rb') as fh:
        unpacked = pickle.load(fh)

    print(unpacked == some_data)
    print(unpacked is some_data)
    print(id(unpacked))
    print(id(some_data))

    print(unpacked)
    print(type(unpacked[2]))
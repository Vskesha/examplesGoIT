import pickle


if __name__ == '__main__':
    some_data = {
        (1, 3, 5): 'tuple',
        2: [1, 2, 3],
        'a': {'key': 'value'}
    }

    byte_string = pickle.dumps(some_data)
    unpacked = pickle.loads(byte_string)

    print(unpacked == some_data)
    print(unpacked is some_data)
    print(id(unpacked))
    print(id(some_data))
    
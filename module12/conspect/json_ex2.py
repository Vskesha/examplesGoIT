import json


if __name__ == '__main__':
    some_data = {
        'key': 'value',
        2: [1, 2, 3],
        'tuple': (5, 6),
        'a': {'key': 'value'}
    }
    file_name = 'data.json'
    with open(file_name, 'w') as fh:
        json.dump(some_data, fh)

    with open(file_name, 'r') as fh:
        unpacked = json.load(fh)

    print(unpacked == some_data)
    print(unpacked is some_data)

    print(unpacked['key'] == some_data['key'])
    print(unpacked['a'] == some_data['a'])
    print(unpacked['2'] == some_data[2])
    print(unpacked['tuple'] == [5, 6])

    print(unpacked)
    print(type(unpacked))

import json


if __name__ == '__main__':
    with open('storage.json', 'r') as f:
        store = json.load(f)

    print(store)
    print(store.get('dict').get('a'))

import json


if __name__ == '__main__':
    d = {'a': 1}
    l = [1, 3, 4]
    t = (3, 4)
    b = True
    s = 'Hello world'
    st = {1, 2, 'Test'}
    obj = {'tuple': t, 'list': l, 'dict': d, 'bool': b, 'str': s, 'none': None}
    print(json.dumps(d))
    print(json.dumps(l))
    print(json.dumps(t))
    print(json.dumps(s))
    print(json.dumps(b))
    print(json.dumps(None))

    with open('storage.json', 'w') as f:
        json.dump(obj, f)

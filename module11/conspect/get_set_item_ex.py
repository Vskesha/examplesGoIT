from collections import defaultdict


class ListedValuesDict:
    def __init__(self):
        self.data = defaultdict(list)

    def __setitem__(self, key, value):
        self.data[key].append(value)

    def __getitem__(self, key):
        return ', '.join(map(str, self.data[1]))


if __name__ == '__main__':
    l_dict = ListedValuesDict()
    l_dict[1] = 'a'
    l_dict[1] = 'b'
    print(l_dict[1])
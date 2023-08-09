from collections import UserDict


class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


if __name__ == '__main__':
    vs_dict = ValueSearchableDict(a=1, b=3)
    print(vs_dict)
    vs_dict['a'] = 10
    vs_dict['c'] = 15
    print(vs_dict)
    print(vs_dict.has_in_values(3))
    print(vs_dict.has_in_values(10))
    print(vs_dict.has_in_values(1))

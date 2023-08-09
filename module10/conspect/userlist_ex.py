from collections import UserList


class CountableList(UserList):

    def sum(self):
        return sum(map(int, self.data))

    def append(self, val):
        super().append(val)
        print(f'{val} was appended to list')


if __name__ == '__main__':
    my_data = [1, '2', 3, '4']
    countable = CountableList(my_data)
    print(countable)
    print(countable.sum())
    countable.append('5')
    print(countable.sum())

# methods __getitem__ and __setitem__
from collections import UserList


class PositiveNumber(UserList):
    def __init__(self, data=None):
        data = data or []
        super(PositiveNumber, self).__init__()
        if data is None:
            data = []
        self.data = list(filter(lambda x: x > 0, data))

    def __getitem__(self, item):
        if item is None:
            return self.data
        return self.data[item]

    def __setitem__(self, key, value):
        if value > 0 and key < len(self.data):
            self.data[key] = value

    def append(self, item) -> None:
        if item > 0:
            super().append(item)


if __name__ == '__main__':
    nums = PositiveNumber([2, -4, 5])
    print(nums)
    print(nums[0])
    print(nums[1])
    print(nums[None])
    nums[1] = -1
    print(nums)
    nums[1] = 3
    print(nums)
    nums[21] = 51
    print(nums)
    nums.append(-5)
    print(nums)
    nums.append(5)
    print(nums)



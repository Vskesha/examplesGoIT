class str(str):

    def __add__(self, other):

        return 1

    def __eq__(self, other):
        if isinstance(other, int):
            return super().__eq__(other.__str__())


if __name__ == '__main__':
    a = str('a')
    b = str('b')
    one = '1'

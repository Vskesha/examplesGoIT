import pickle


class MyReader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def __repr__(self):
        return f'MyReader({repr(self.file)}, {repr(self.position)})'

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position += self.fh.tell()
        return data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])


if __name__ == '__main__':
    my_reader = MyReader('names.csv')
    print(my_reader)

    print(my_reader.read(21))
    print(my_reader)

    with open('savedmyreader.bin', 'wb') as fh:
        pickle.dump(my_reader, fh)

    print(my_reader.read(12))
    print(my_reader.read(11))
    print(my_reader.read(15))
    print(my_reader.read(10))
    my_reader.close()
    print('my_reader closed')
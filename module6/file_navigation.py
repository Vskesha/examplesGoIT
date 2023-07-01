def main():
    fh = open('test4.txt', 'w+')
    fh.write('hello!')

    fh.seek(1)
    second = fh.read(1)
    print(second)
    fh.close()

    fh = open('test5.txt', 'w+')
    fh.write('hello!')

    position = fh.tell()
    print(position)

    fh.seek(1)
    position = fh.tell()
    print(position)

    fh.read(2)
    position = fh.tell()
    print(position)

    fh.close()


if __name__ == '__main__':
    main()

def main():
    fh = open('../../module4/Lecture8/ex_10.py')
    try:
        fh1 = open('ex_10.py')
    except FileNotFoundError:
        print("FileNotFoundError: [Errno 2] No such file or directory: 'ex_10.py'")
    fh.close()

    fh = open('test.txt', 'w')
    symbols_written = fh.write('hello!')
    print(symbols_written)
    fh.close()

    fh = open('test.txt', 'w+')
    fh.write('hello!')
    last_two = fh.read(2)
    print(last_two)
    fh.seek(0)
    first_two_symbols = fh.read(2)
    print(first_two_symbols)
    fh.close()


if __name__ == '__main__':
    main()

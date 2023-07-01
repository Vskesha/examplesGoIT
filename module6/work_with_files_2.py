def main():
    fh = open('test2.txt', 'w')
    fh.write('Hello!')
    fh.close()

    fh = open('test2.txt', 'r')
    all_file = fh.read()
    print(all_file)
    fh.close()

    fh = open('test2.txt', 'r')
    while True:
        symbol = fh.read(1)
        if len(symbol) == 0:
            break
        print(symbol)
    fh.close()


if __name__ == '__main__':
    main()

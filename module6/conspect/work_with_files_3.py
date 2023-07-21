def main():
    fh = open('test3.txt', 'w')
    fh.write('first line\nsecond line\nthird line')
    fh.close()

    fh = open('test3.txt', 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        print(line)
    fh.close()

    fh = open('test3.txt', 'r')
    lines = fh.readlines()
    print(lines)
    fh.close()


if __name__ == '__main__':
    main()

def main():
    with open('raw_data.bin', 'wb') as fh:
        fh.write(b'Hello world')

    with open('raw_data.bin', 'rb') as f:
        first_four = f.read(4)
        print(first_four)
        the_rest = f.read()
        print(the_rest)


if __name__ == '__main__':
    main()

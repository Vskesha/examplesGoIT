def some_not_useful_function(f):
    raise FileNotFoundError


def main():
    fh = open('test.txt')
    try:
        some_not_useful_function(fh)
    except:
        print('inside except block')
    finally:
        fh.close()

    with open('test.txt') as fh:
        some_not_useful_function(fh)


if __name__ == '__main__':
    main()

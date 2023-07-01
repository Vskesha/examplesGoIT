def main():
    fh = open('test.txt')
    try:
        some_useful_function(fh)
    except:
        print('inside except block')
    finally:
        fh.close()

    with open('test.txt') as fh:
        some_useful_function(fh)


if __name__ == '__main__':
    main()

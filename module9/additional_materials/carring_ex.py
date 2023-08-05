def greeting(mode):
    return MODES.get(mode)


def hello_male(name):
    print(f'Mr. {name}')


def hello_female(name):
    print(f'Mrs. {name}')


def hello_pan(name):
    print(f'Pan {name}')


MODES = {
    'm': hello_male,
    'f': hello_female,
    'pan': hello_pan,
}


def main():
    mr = greeting('m')
    mrs = greeting('f')
    pan = greeting('pan')

    mr('Vasyl')
    mrs('Mariya')
    pan('Mykola')


if __name__ == '__main__':
    main()

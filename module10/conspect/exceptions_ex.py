import string


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input('Enter name: ')
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


if __name__ == '__main__':
    while True:
        try:
            name = enter_name()
            break
        except NameTooShortError:
            print("Name is too short, need more than 3 symbols. Try again.")
        except NameStartsFromLowError:
            print('Name should start with capital letter. Try again.')
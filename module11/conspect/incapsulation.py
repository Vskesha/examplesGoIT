class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


if __name__ == '__main__':
    s = Secret()
    print(s.public_field)
    print(s._private_field)
    print(s._Secret__real_secret)
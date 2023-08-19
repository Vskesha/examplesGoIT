class KeyStore:
    def __init__(self, name, password):
        self.__name = None
        self.__password = None
        self.__secret = None
        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def password(self):
        return 'No way to get password'

    @password.setter
    def password(self, new_password):
        if self.__password is None:
            self.__password = new_password
        elif self.is_validate():
            self.__password = new_password

    @property
    def secret(self):
        if self.is_validate():
            return self.__secret

    @secret.setter
    def secret(self, value):
        if self.is_validate():
            self.__secret = value

    def is_validate(self):
        p = input('Password: ')
        if self.__password == p:
            print('Ok')
            return True
        print('Wrong password')
        return False


if __name__ == '__main__':
    key_srore = KeyStore('Oksana', '123456')
    print('Read password')
    print(key_srore.password)
    key_srore.password = '567234'
    print('Set secret value')
    key_srore.secret = 'Test'
    print('Read secret value')
    print(key_srore.secret)

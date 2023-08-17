class Character:

    def __init__(self, name):
        self.name = name   # public
        self._damage = 10  # protected
        self.__hp = 100    # private

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 0 < value <= 100:
            self.__hp = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 < value <= 100:
            self.__hp = value
        else:
            raise ValueError('HP should be in range 1-100')

    def func(self):
        self._damage

    def public(self):
        pass

    def _protected(self):
        pass

    def __private(self):
        pass


class Enemy(Character):

    def func(self):
        self._damage


if __name__ == '__main__':
    char = Character('vasya')
    char._damage  # incorect

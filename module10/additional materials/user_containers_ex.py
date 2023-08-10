from collections import UserDict, UserList


class Phones(UserList):
    def set_phone(self, phone):
        new_phone = phone
        if len(phone) == 12:
            new_phone = '+' + phone
        elif len(phone) == 10:
            new_phone = '+38' + phone
        self.data.append(new_phone)

    def get_phones(self):
        return self.data


class User(UserDict):
    def set_name(self, name):
        self.data['name'] = name

    def get_name(self):
        return self.data.get('name')

    def set_phone(self, phone):
        phone_list = self.data.get('phones', Phones())
        phone_list.set_phone(phone)
        self.data['phones'] = phone_list

    def get_phones(self):
        return self.data.get('phones', Phones())


if __name__ == '__main__':
    phone_list = Phones()
    phone_list.set_phone('0989008080')
    phone_list.set_phone('38068007070')
    print(phone_list.get_phones())

    user1 = User()
    user1.set_name('Bill')
    user1.set_phone('0989008080')
    user1.set_phone('380968007070')
    print(user1.get_name(), user1.get_phones())

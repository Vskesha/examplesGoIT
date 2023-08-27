import pickle
from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.file = 'address_book.bin'
        self.records = self.data
        self.last_record_id = 111111

    def dump(self):
        with open(self.file, 'wb') as file:
            pickle.dump((self.last_record_id, self.records), file)

    def load(self):
        # if not self.file.exists():
        #     return
        with open(self.file, 'rb') as file:
            self.last_record_id, self.records = pickle.load(file)
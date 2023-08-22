from csv import DictWriter
import json


file_json = 'users.json'
file_csv = 'users.csv'


def get_users():
    with open(file_json, 'r') as reader:
        users = json.load(reader)
        return users


def write_table():
    users = get_users()
    with open(file_csv, 'w', encoding='utf-8', newline='') as file:
        fields_names = list(users[0].keys())
        writer = DictWriter(file, delimiter=';', fieldnames=fields_names)
        writer.writeheader()
        for user in users:
            writer.writerow(rowdict=user)
        print('CSV table was created')


if __name__ == '__main__':
    write_table()

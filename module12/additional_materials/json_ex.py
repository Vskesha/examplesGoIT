from faker import Faker
import json


fake = Faker('uk_UA')
users = []


def create_users(fake: Faker, users: list, n=10):
    for _ in range(n):
        user = {}
        user['name'] = fake.name()
        user['phone_number'] = fake.phone_number()
        user['email'] = fake.email()
        user['address'] = fake.address()
        user['birthday'] = fake.date()
        users.append(user)
    to_json(users)


def to_json(users):
    with open('users.json', 'w') as fh:
        json.dump(users, fh, indent=4, ensure_ascii=False)
        print("Users were saved to 'users.json'.")


if __name__ == '__main__':
    create_users(fake, users, 120)

import pickle


FILENAME = 'users.dat'
if __name__ == '__main__':
    users = [
        ['Tom', 28, True],
        ['Alice', 23, False],
        ['Bob', 34, False]
    ]

    with open(FILENAME, 'wb') as file:
        pickle.dump(users, file)

    with open(FILENAME, 'rb') as file:
        user_from_file = pickle.load(file)
        for user in user_from_file:
            print('Name:', user[0], '\tAge:', user[1], '\tStatus:', user[2])

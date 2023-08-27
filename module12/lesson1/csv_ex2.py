import csv


FILENAME = 'users.csv'


if __name__ == '__main__':
    users = [
        {'name': 'Микита', 'age': 22, 'sex': 'male'},
        {'name': 'Alice', 'age': 21, 'sex': 'female'},
        {'name': 'Іван', 'age': 22, 'sex': 'male'},
    ]

    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        columns = ['name', 'age', 'sex']
        writer = csv.DictWriter(f, delimiter=',', fieldnames=columns)
        writer.writeheader()
        for row in users:
            writer.writerow(row)

    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # print(row['name'])
            print(row)

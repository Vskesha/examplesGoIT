import csv


if __name__ == '__main__':
    with open('names.csv', 'w', newline='') as fh:
        field_names = ['first_name', 'last_name']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    with open('names.csv', 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            print(row["first_name"], row["last_name"])

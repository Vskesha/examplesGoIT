import csv


if __name__ == '__main__':
    with open('names.csv', 'w', newline='\n') as csvfile:
        field_names = ['first_name', 'last_name']

        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({'first_name': 'Tony', 'last_name': 'Stark'})
        writer.writerow({'first_name': 'Bob', 'last_name': 'Smith'})
        writer.writerow({'first_name': 'Alice', 'last_name': 'Stark'})

    with open('names.csv', 'r', newline='\n') as csvfile:
        print(csvfile.read())


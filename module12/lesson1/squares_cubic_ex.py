import csv


N = 20


if __name__ == '__main__':
    name = 'table.csv'
    with open(name, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for i in range(1, N + 1):
            writer.writerow([i, i ** 2, i ** 3])

    with open(name, 'r', newline='\n') as file:
        reader = csv.reader(file)
        res = []
        for row in reader:
            res.append(row)

    print(res)
import csv


if __name__ == '__main__':
    c_codes = {}
    name = 'countries.csv'
    with open(name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            c_codes[line[0]] = line[1]
        c_codes.pop('Code')
    print(c_codes['UA'])
    print(c_codes)
    
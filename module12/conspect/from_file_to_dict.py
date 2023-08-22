if __name__ == '__main__':
    file_name = 'expenses.txt'
    expences = {}
    with open(file_name, 'r') as fh:
        raw_expences = fh.readlines()
        for line in raw_expences:
            key, value = line.split("|")
            expences[key] = int(value)

    print(expences)
from string import ascii_uppercase


def find_column_index(column_name: str) -> int:
    letter_mapping = {char: idx for idx, char in enumerate(ascii_uppercase, 1)}
    res = 0
    for char in column_name:
        res = res * 26 + letter_mapping.get(char, 0)
    return res


print(find_column_index('AAA'))

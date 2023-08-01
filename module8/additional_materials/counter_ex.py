from collections import Counter


def get_count_chars(text) -> dict:
    count_dict = {}
    for c in text:
        count_dict[c] = count_dict.get(c, 0) + 1
    return count_dict


if __name__ == '__main__':
    text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
            'sed do eiusmod tempor incididunt ut labore et dolore magna '
            'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
            'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
            'Duis aute irure dolor in reprehenderit in voluptate velit '
            'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
            'occaecat cupidatat non proident, sunt in culpa qui officia '
            'deserunt mollit anim id est laborum.')

    print(get_count_chars(text))

    counter = Counter(text)
    print(counter)
    print(counter.most_common(5))
    print(sorted(counter))

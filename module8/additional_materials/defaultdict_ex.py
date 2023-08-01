from collections import defaultdict


def get_word_list(text):
    word_list = text.split()
    word_dict = {}
    for word in word_list:
        words = word_dict.get(word[0])
        if words:
            words.append(word)
        else:
            word_dict[word[0]] = [word]
    return word_dict


def get_word_list_dd(text):
    word_list = text.split()
    word_dict = defaultdict(list)
    for word in word_list:
        word_dict[word[0]].append(word)
    return word_dict


if __name__ == '__main__':
    text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
            'sed do eiusmod tempor incididunt ut labore et dolore magna '
            'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
            'ullamco laboris nisi ut aliquip ex ea commodo consequat. '
            'Duis aute irure dolor in reprehenderit in voluptate velit '
            'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint '
            'occaecat cupidatat non proident, sunt in culpa qui officia '
            'deserunt mollit anim id est laborum.')

    word_dict = get_word_list(text)
    print(word_dict)

    word_dict_dd = get_word_list_dd(text)
    print(word_dict_dd)

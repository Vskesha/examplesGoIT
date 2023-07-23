def data_preparation(list_data):
    result = []
    for lst in list_data:
        if len(lst) < 3:
            continue
        lst.remove(max(list))
        lst.remove(min(list))
        result.extend(lst)
    result.sort(reverse=True)
    return result


if __name__ == '__main__':
    data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]])
    # [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]] поверне наступний список [6, 5, 3, 2, 2, 1]
    data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]])
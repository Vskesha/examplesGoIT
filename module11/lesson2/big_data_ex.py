from time import time
import resource


def read_file(filename):
    text_file = open(filename, 'r')
    lines = text_file.readlines()
    text_file.close()
    return lines


def read_file_yield(filename):
    text_file = open(filename, 'r')
    while True:
        line = text_file.readline()
        if not line:
            text_file.close()
            break
        yield line


if __name__ == '__main__':
    start = time()
    data = read_file('data.txt')
    print(type(data))
    print(f'Used time: {time() - start}')
    print('Peak memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    # Used time: 1.463477373123169
    # Peak memory usage:  2329428

    # Used time: 0.429764986038208
    # Peak memory usage: 2329428

    start = time()
    data = read_file_yield('data.txt')
    print(type(data))
    print(f'Used time: {time() - start}')
    print('Peak memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

def main():
    s = b'Hello!'
    print(s[1])

    byte_string = b'Hello world!'
    print(byte_string)

    byte_str = 'some text'.encode()
    print(byte_str)

    numbers = [0, 105, 128, 255]
    byte_numbers = bytes(numbers)
    print(byte_numbers)

    nums = [127, 255, 156]
    some_numbers = bytes(nums)
    print(some_numbers)
    for num in nums:
        print(hex(num))

    print(ord('a'))
    print(chr(100))

    s = 'Привіт!'
    utf8 = s.encode()
    print(f'{utf8}')
    utf16 = s.encode(encoding='utf-16')
    print(f'{utf16}')
    utf32 = s.encode(encoding='utf-32')
    print(f'{utf32=}')
    s_from_utf16 = utf16.decode(encoding='utf-16')
    print(f'{s_from_utf16=}')
    print(s == s_from_utf16)

    print(b'Hello world!'.decode('utf-16'))


if __name__ == '__main__':
    main()

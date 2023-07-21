def main():
    byte_array = bytearray(b'Kill Bill')
    byte_array[0] = ord('B')
    byte_array[5] = ord('K')
    print(byte_array)

    print(byte_array[0])




if __name__ == '__main__':
    main()

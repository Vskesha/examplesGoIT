def main():
    s = 'VsKesha Vasyl Boliukh'

    ans = ''

    for c in filter(lambda x: x.islower(), s):
        ans += c

    print(ans)


if __name__ == '__main__':
    main()
    
   
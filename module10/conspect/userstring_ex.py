from collections import UserString


class TruncatedString(UserString):
    # def __init__(self, *args, max_len):
    #     super().__init__(*args)
    #     self.max_len = max_len

    def truncate(self, length):
        self.data = self.data[:length]


if __name__ == '__main__':
    ts = TruncatedString('abcdefghjklmnop')
    print(f"{ts=}")
    ts.truncate(7)
    print(f"Truncated 7 {ts=}")
    ts.truncate(3)
    print(f"Truncated 3 {ts=}")
    ts.truncate(10)
    print(f"Truncated 10 {ts=}")

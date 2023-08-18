from datetime import datetime
from time import sleep


class FileReader:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.log = ''
        self.timestamp = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        msg = '{:<20}|{:^15}| open\n'.format(self.timestamp, self.filename)
        self.log += msg
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            timestamp_end = datetime.now().timestamp()
            diff = timestamp_end - self.timestamp
            msg = '{:<20}|{:^15}| closed {:>15} s\n'.format(timestamp_end, self.filename, diff)
            self.log += msg
            self.opened = False


if __name__ == '__main__':
    reader = FileReader('new_file.txt')

    with reader as f:
        sleep(2)
        print(f.read())

    with reader as f:
        sleep(1)
        print(f.read())

    print(reader.log)
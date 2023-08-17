class Iterator:

    def __init__(self, start=0, stop=100, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        # print(f'Hey I am iteration number {self.start}')

        if self.start >= self.stop:
            raise StopIteration
        ret = self.start
        self.start += self.step
        
        return ret
    
    def __iter__(self):
        return self



if __name__ == '__main__':
    my_iterator = Iterator(20, 40, 10)

    for i in my_iterator:
        print(i)

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position_list = [self.x, self.y]
        self.position_dict = {'x': self.x, 'y':self.y}

    def __str__(self):
        return f'str: ({self.x}, {self.y})'

    def __repr__(self):
        return f'Position({self.x}, {self.y})'
        
    def __getitem__(self, key):
        print(f'You are trying to get an element with key {key}')
        if key == 0 or key == 'x':
            return self.x
        elif key == 1 or key == 'y':
            return self.y
        else:
            raise IndexError('Index could be either 0 or 1 or "x" or "y"')
        

    def __setitem__(self, key, value):
        if key == 0 or key == 'x':
            self.x = value
            self.position_list[0] = value
            self.position_dict['x'] = value
        elif key == 1 or key == 'y':
            self.y = value
            self.position_list[1] = value
            self.position_dict['y'] = value
        else:
            raise IndexError('Index could be either 0 or 1 or "x" or "y"')
        
    def __call__(self, a=0):
        print('This object has been called')
        print(a)

    def __enter__(self):

        print('Entering the context manager')
        return self


    def __exit__(self, exc_type, exc_value, traceback):

        print('Finishing context manager')
        
        if exc_type is not None:
            print(f'There was an exception: {exc_type}: {exc_value}\n{traceback}')

        
if __name__ == '__main__':
    char_position = Position(1, 3)
    
    with char_position as c_p:
        raise ValueError('bla bla bla')
        print(c_p)

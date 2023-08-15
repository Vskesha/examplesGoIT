class Session:
    def __init__(self, addr, port=8080):
        self.connected = False
        self.addr = addr
        self.port = port

    def __enter__(self):
        self.connected = True
        print(f'Connected to {self.addr}:{self.port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print('Some error!')
        else:
            print('No problem!')


if __name__ == '__main__':
    localhost_session = Session('localhost')

    with localhost_session as session:
        print(session is localhost_session)
        print(session.connected)
    print(session.connected)

    with localhost_session as session:
        print(session is localhost_session)
        print(session.connected)
    print(session.connected)

    with Session('host', 7711) as session:
        print(session.connected)
        raise Exception('OH NO!')
    print(session.connected)
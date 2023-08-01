from collections import deque


def main():
    queue = deque(maxlen=10)
    for i in range(20):
        queue.appendleft(i)
    print(queue)
    start = queue.popleft()
    end = queue.pop()
    print(start)
    print(end)


def menu():

    user_inputs = deque(maxlen=10)

    while True:
        user_input = input('>>> ')
        user_inputs.append(user_input)
        if user_input == 'q':
            break

    print('Good bye')
    print(f'User steps: {user_inputs}')


if __name__ == '__main__':
    # main()
    menu()
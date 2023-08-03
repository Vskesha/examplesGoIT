from datetime import datetime
from collections import deque


def insert_in_list():
    my_list = []

    for i in range(10_000):
        my_list.insert(0, i)


def insert_in_deque():
    my_deque = deque()

    for i in range(10_000):
        my_deque.appendleft(i)


n = 100
list_times = []
deque_times = []

for i in range(n):
    start = datetime.now().timestamp()
    insert_in_list()
    end = datetime.now().timestamp()
    result = end - start
    list_times.append(result)
    
for i in range(n):
    start = datetime.now().timestamp()
    insert_in_deque()
    end = datetime.now().timestamp()
    result = end - start
    deque_times.append(result)
    
print(sum(list_times) / n)
print(sum(deque_times) / n)

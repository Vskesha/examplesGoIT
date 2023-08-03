from datetime import datetime


def for_generator():
    my_list = []

    for i in range(1_000_000):
        my_list.append(i)


def comprehensions_generator():
    my_list = [i for i in range(1_000_000)]
    

n = 300
for_times = []
comprehensions_times = []

for i in range(n):
    start = datetime.now().timestamp()
    for_generator()
    end = datetime.now().timestamp()
    result = end - start
    for_times.append(result)
    
for i in range(n):
    start = datetime.now().timestamp()
    comprehensions_generator()
    end = datetime.now().timestamp()
    result = end - start
    comprehensions_times.append(result)

print(sum(for_times) / n)
print(sum(comprehensions_times) / n)

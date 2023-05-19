import random

def list_to_dict(data):
    return {(key ** 3): key for key in data}

n = int(input())
a = []
for i in range(10):
    a.append(random.randint(1, n))

s = []
for i in range(len(a)):
    s.append(a[i])

print(list_to_dict(a))
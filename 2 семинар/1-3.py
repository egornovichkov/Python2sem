import random

def list_to_dict(data):
    return {key: (key ** 2) for key in data}

a = []
for i in range(10):
  a.append(random.uniform(0, 100))

s = []
for i in range(len(a)):
    s.append(a[i])

print(list_to_dict(a))
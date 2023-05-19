def list_to_dict(data):
    return {key: key for key in data}

a = str(input())
a = sorted(a)
dictionary = list_to_dict(a)

for i in range(len(dictionary)):
  dictionary[list(dictionary)[i]] = a.count(list(dictionary)[i])
print(dictionary)
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

x = abs(x1 - y1)
y = abs(x2 - y2)

def f(x, y):
  if (x > y and x >= 2 and y >= 1) or x == y and x != 1:
    return (x - 2, y - 1) 
  elif y > x and y >= 2 and x >= 1:
    return (x - 1, y - 2)
  elif x == 1 and y == 1:
    return (x, y)

s = 0
while x > 0 or y > 0:
  s += 1
  x, y = f(x, y)
  if x == y == 1:
    s += 2
    break

print(s)
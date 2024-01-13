import math
x1 = 3
y1 = -2
x2 = -1
y2 = 7

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

result = distance(x1, y1, x2, y2)
print(result)

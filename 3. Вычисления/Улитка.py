from math import ceil
h = int(input())
a = int(input())
b = int(input())

n = (h - a) / (a - b)
print(ceil(n) + 1)
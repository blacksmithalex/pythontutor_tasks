a = [int(x) for x in input().split()]
X = int(input())
pos = 0
while pos < len(a) and X <= a[pos]:
    pos += 1
print(pos + 1)


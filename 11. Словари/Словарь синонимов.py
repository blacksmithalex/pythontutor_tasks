syn = {}
n = int(input())
for _ in range(n):
    a, b = input().split()
    syn[a] = b
    syn[b] = a
print(syn[input()])
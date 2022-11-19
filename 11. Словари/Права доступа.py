short = {'read': 'R', 'write': 'W', 'execute': 'X'}
files = {}
n = int(input())
for _ in range(n):
    line = input().split()
    files[line[0]] = line[1:]

k = int(input())
for _ in range(k):
    c, f = input().split()
    if short[c] in files[f]:
        print('OK')
    else:
        print('Access denied')

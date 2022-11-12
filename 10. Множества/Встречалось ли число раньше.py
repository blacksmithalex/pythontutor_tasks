words = set()

r = input().split()
for x in r:
    if x in words:
        print('YES')
    else:
        print('NO')
        words.add(x)

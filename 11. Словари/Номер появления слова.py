words = input().split()
d = {}
for w in words:
    if w not in d:
        print(0)
        d[w] = 1
    else:
        print(d[w])
        d[w] += 1

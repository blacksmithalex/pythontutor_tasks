d = {}
n = int(input())
for _ in range(n):
    eng, latin = input().split(' - ')
    latin = latin.split(', ')
    for l in latin:
        d[l] = d.get(l, []) + [eng]
print(len(d))
for word in sorted(d):
    print(word, '-', ', '.join(sorted(d[word])))


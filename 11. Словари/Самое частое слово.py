d = {}
n = int(input())
for _ in range(n):
    words = input().split()
    for w in words:
        d[w] = d.get(w, 0) + 1

res = [w for w in d if d[w] == max(d.values())]
print(min(res))

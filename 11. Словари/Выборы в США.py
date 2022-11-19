d = {}
n = int(input())
for _ in range(n):
    cand, num = input().split()
    num = int(num)
    d[cand] = d.get(cand, 0) + num

for cand in sorted(d):
    print(cand, d[cand])
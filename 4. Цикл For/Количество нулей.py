N = int(input())
count0 = 0
for _ in range(N):
    if int(input()) == 0:
        count0 += 1
print(count0)
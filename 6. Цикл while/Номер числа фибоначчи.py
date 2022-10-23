a = int(input())
if a == 0:
    print(0)
else:
    prev, cur = 0, 1
    n = 1
    while cur <= a:
        if cur == a:
            print(n)
            break
        prev, cur = cur, prev + cur
        n += 1
    else:
        print(-1)
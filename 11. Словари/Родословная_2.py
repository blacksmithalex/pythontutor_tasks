def is_ancestor(man, older_man):
    while man in d:
        man = d[man]
        if man == older_man:
            return True
    return False

N = int(input())
d = {}
for _ in range(N - 1):
    f, s = input().split()
    d[f] = s

K = int(input())
for _ in range(K):
    f, s = input().split()
    if is_ancestor(f, s):
        print(2)
    elif is_ancestor(s, f):
        print(1)
    else:
        print(0)



def capitalize(a):
    first = chr(ord(a[0]) - 32)
    return first + a[1:]

print(*[capitalize(a) for a in input().split()])
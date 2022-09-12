a = [int(x) for x in input().split()]
IMi, IMa = a.index(min(a)), a.index(max(a))
a[IMi], a[IMa] = a[IMa], a[IMi]

print(*a)
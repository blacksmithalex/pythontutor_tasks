a = input()

ind = (len(a) + 1) // 2
a = a[ind:] + a[:ind]
print(a)
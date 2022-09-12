a = input()
l, r = a.find('h'), a.rfind('h')
print(a[:l] + a[l:r + 1][::-1] + a[r + 1:])


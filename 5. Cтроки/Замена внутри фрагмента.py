a = input()
l, r = a.find('h'), a.rfind('h')
print(a[:l + 1] + a[l + 1:r].replace('h', 'H') +  a[r:])
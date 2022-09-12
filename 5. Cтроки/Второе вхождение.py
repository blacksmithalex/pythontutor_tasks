a = input()
if a.count('f') == 0:
    print(-2)
elif a.count('f') == 1:
    print(-1)
else:
    f1 = a.find('f')
    print(a.find('f', f1 + 1))
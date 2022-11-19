cust = {}
while True:
    try:
        name, goods, num = input().split()
        num = int(num)
        if name not in cust:
            cust[name] = {}
            prod = cust[name]
            prod[goods] = num
        else:
            prod = cust[name]
            prod[goods] = prod.get(goods, 0) + num
    except:
        break

for c in sorted(cust):
    print(c + ':')
    goods = cust[c]
    for g in sorted(goods):
        print(g, goods[g])
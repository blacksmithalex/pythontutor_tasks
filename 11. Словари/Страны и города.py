d = {}
n = int(input())
for _ in range(n):
    country, *cities = input().split()
    for city in cities:
        d[city] = country

n = int(input())
for _ in range(n):
    print(d[input()])
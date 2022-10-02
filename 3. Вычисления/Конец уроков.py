n = int(input())
count5 = (n - 1) // 2 + (n - 1) % 2
count15 = (n - 1) // 2

min = n * 45 + count5 * 5 + count15 * 15
h, m = min // 60, min % 60
print(9 + h, m)

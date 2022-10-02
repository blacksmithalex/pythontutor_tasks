P = int(input())
X = int(input())
Y = int(input())

cop = (X * 100 + Y) * (100 + P) / 100
print(int(cop // 100), int(cop % 100))
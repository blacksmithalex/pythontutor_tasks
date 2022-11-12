n = int(input())
words = set()
for _ in range(n):
    a = input().split()
    words.update(set(a))
print(len(words))

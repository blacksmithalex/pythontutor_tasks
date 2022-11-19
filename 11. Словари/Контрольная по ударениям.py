def f(word):
    count = 0
    for l in word:
        if l == l.capitalize():
            count += 1
    return count == 1

d = {}
n = int(input())
for _ in range(n):
    word = input()
    d[word.capitalize()] = d.get(word.capitalize(), []) + [word]

words = input().split()
nwrong = 0
for w in words:
    if w.capitalize() in d:
        if w not in d[w.capitalize()]:
            nwrong += 1
    else:
        if f(w) == False:
            nwrong += 1
print(nwrong)

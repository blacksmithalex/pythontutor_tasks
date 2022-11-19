freq = {}
n = int(input())
for _ in range(n):
    words = input().split()
    for w in words:
        freq[w] = freq.get(w, 0) + 1

pairs = []
for w in freq:
    pairs.append([-freq[w], w])

for pair in sorted(pairs):
    print(pair[1])
n = int(input())
var = set([str(i) for i in range(1, n + 1)])

read = input()
while read != 'HELP':
    read = set(read.split())
    if_yes = var & read
    if_no = var - read
    if len(if_yes) <= len(if_no):
        print('NO')
        var -= read
    else:
        print('YES')
        var &= read
    read = input()
for x in sorted([int(x) for x in var]):
    print(x, end=' ')



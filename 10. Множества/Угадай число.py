n = int(input())
var = set([str(x) for x in range(1, n + 1)])

read = input()
while read != 'HELP':
    answer = input()
    if answer == 'YES':
        var &= set(read.split())
    elif answer == 'NO':
        var -= set(read.split())
    read = input()

for x in sorted(var):
    print(x, end = ' ')

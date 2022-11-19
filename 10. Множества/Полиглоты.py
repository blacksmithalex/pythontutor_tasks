set_1 = set() #все языки
set_2 = set() #языки, которые знает каждый школьник

n = int(input())
for _ in range(n):
    num = int(input())
    langs = []
    for _ in range(num):
        langs.append(input())
    set_1.update(set(langs))
    if len(set_2) == 0:
        set_2.update(set(langs))
    else:
        set_2.intersection_update(set(langs))

for var in [set_2, set_1]:
    print(len(var))
    for lang in sorted(var):
        print(lang)
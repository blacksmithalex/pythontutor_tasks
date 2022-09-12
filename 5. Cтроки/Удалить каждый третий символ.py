a = input()
acopy = '' 

for i in range(len(a)):
    if i % 3 == 0:
        continue 
    acopy += a[i]
a = acopy

print(a)
    
    
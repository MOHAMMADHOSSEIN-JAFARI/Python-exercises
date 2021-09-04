a = int(input())
print(a)
b = input().split() 
print(b)
b = map(int, b)
print(b)
b = sorted(b)
print(b)
count= 0
for i in b:
    if i <= 2:
        count+= 1
    else: 
        count= count
print(count // 3)
        
### the else part can also not be written
    



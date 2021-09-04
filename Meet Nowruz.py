a = int(input())
b = input().split() 
b = map(int, b)
b = sorted(b)
count= 0
for i in b:
    if i <= 2:
        count+= 1
    else: 
        count= count
print(count // 3)
        
        
    



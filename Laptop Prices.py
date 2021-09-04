c = []
a = int(input())
for i in range(1, a+1):
    b = input().split() 
    print(b)
    b = map(int, b)
    b = sorted(b)
    c.append(b)

count= 0
final= 0
for i in c: 
    
    
    z= c.pop(count)
    
    for j in c :
        if i[0] > j[0] and  i[1] < j[1]:
            final += 1
    
    c.insert(count, i)  
    count += 1
if final > 0:
    print('happy irsa')       
else:
    print("poor irsa")
            
print(c)
    
    
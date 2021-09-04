a = int(input())
english = []
farsi = []
for i in range(1, a+1):
    b = input().split()
    english.append(b[0])
    farsi.append(b[1])   
res = {}
for i in range (0,a):
    res[english[i]] = farsi[i]

g= input().split()

trans= []

for z in g:
    if z in english:
        trans.append(res[z])
    else: 
        trans.append(z)
 
for w in trans:
    print(w, end=" ")
    
    
    





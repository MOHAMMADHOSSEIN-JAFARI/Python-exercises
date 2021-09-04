import math
a= int(input())
root = []
new= []
for s in range(1, a+1):
   vorodi = float(input())
   jazr = math.sqrt(vorodi)
   root.append(jazr)
root= list(map(str,root ))
for i in root:
    b= i.split('.')
   
    if len(b[1]) >= 4:
        c= b[0]+ '.'+ b[1][:4]
        new.append(c)
    elif len(b[1]) == 3:
        c= b[0]+ '.'+ b[1][:3]+ '0'
        new.append(c)
    elif len(b[1]) == 2:
        c= b[0]+ '.'+ b[1][:2]+ '00'
        new.append(c)
    elif len(b[1]) == 1: 
        c= b[0]+ '.'+ b[1]+ '000'
        new.append(c)
    
for z in new:
    print(z)
    
         
    
        
        
        
        
        
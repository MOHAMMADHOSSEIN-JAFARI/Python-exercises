a = input()
b = a[::2]#eliminating the + sign 

c = ''.join(sorted(b))

newstring = ''
for i in c:
    newstring+='+'
    newstring+=i
print(newstring[1:])# eliminating the first + sign

    

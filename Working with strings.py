z = input()
z = z.lower() 
newstring = ''
for i in z:
  if not i in 'aeiou':
    newstring+='.'
    newstring+=i  
print(newstring)


a = input()
b =  sum(1 for c in a if c.isupper())
e =  sum(1 for d in a if d.islower())
if b > e: 
    print(a.upper())
else:
    print(a.lower())

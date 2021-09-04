a = int(input())

c = []
counter= dict()
for i in range(1,a+1):
    b= input()
    c.append(b)

for letter in c: 
     if letter in counter: 
        counter[letter] += 1
     else: 
        counter[letter]= 1
import collections
od = collections.OrderedDict(sorted(counter.items()))
for k, v in od.items():
    print(k, v)   
 
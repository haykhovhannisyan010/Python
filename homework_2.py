#Ruben
#1 
n = input()
nums = []
d = {}
while n != "End":
    nums.append(n)
    n = input()
for m in nums:
    if m in d:
        continue
    else:
        d[int(m)] = nums.count(m)
print(d)

#2
word = input()
c = 0
a = 0
elements = {c:word.count(c) for c in set(word)}
for e in elements.values():
    if e % 2 == 0:
        c += 1
    else:
        c -= 1
        a += 1
if c > 0:
    even = True
else:
    even = False
if even == True or (len(word) % 2 == 1) and a  == 1:
    print(True)
else:
    print(False)
    
#Narek 
#1
for i in range(100):
    for j in range(100):
        if i ** j == j**i and i!= j:
            print(i,j,i**j, )
    

#2 
for row in range(1,5):
    for i in range(1,row+1):
        print(row, end=" ")  
    #print(" ")

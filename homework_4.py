#Narek
#1
a = [2,8,5,3,4,6,7]
minn = b = 0
c = []
for j in range(2,max(a)): 
    for i in a:
        if i % j != 0:
            minn+= 1
            if minn == len(a):
                b = j
                c.append(b)
        else:
            minn = 0
            break
print(min(c) if c else max(a)+1)
               
#2
n = "2x+15-1+2=35"
c = 0
for i in range(len(n)):
    c += 1
    if n[i] == "=":
        break
a = n[:c-1]
b = [n[c:]]
h = [n[c:]]
x = []
for j in range(len(a)):
    if not "x" in a[j]:
        if a[j] == "+":
            b.append("-")
        elif a[j] == "-":
            b.append("+")
        else:
            b.append(a[j])
    else:
        while h != b:
            if b[-1] != "+" or b[-1] != "-":
                x.append(b[-1])
                b.pop()
                break
b = "".join(b)
x.reverse()
x = "".join(x)
if x:
    print(eval(b) / int(x[0]))
else:
    print(eval(b))
    
    
#Ruben
#2
string = input()
vowel={}
consonant={}
l = []
for i in range(len(string)):
    if string[i] in "aeoiu":
        l.append(i)
        b = string
        for j in b[i+1:]:
            print(b + j)
            b += j
            
print(l)

#Narek
#1
def absolute(l):
    c = 0
    for i in range(1,len(l)):
        if c < abs(l[i] - l[i-1]):
            c = abs(l[i] - l[i-1])
    return c

print(absolute([5,9,2,12,5,8]))

#2
def c(n):
    c = 0
    a = []
    for i in range(n+1):
        a.append(str(i))
    a = "".join(a)
    for i in range(len(a)):
        if a[i] == "2":
            c += 1
    return c 
        
    
print(c(22))
    
        
    
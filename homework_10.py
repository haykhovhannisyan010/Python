<<<<<<< HEAD
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
def count_of2s_in_range(n):
    count=0
    n_string=str(n)
    curent=int(n_string[0])
    if int(n_string[0])>2:
        count+=10**(len(n_string)-1)
    elif int(n_string[0])==2:
        count+=n-(2*(10**(len(n_string)-1)))+1
    for i in range(1,len(n_string)):
        if int(n_string[i]) > 2:
            count += (10 ** (len(n_string) - 1-i))*(curent+1)
            curent=int(n_string[0:i+1])
        elif int(n_string[i]) < 2:
            count += (10 ** (len(n_string) - 1-i) * curent)
            curent = int(n_string[0:i + 1])
        else:
            count += (10 ** (len(n_string) - 1-i) * curent+(int(n_string[i:])-(2*(10**(len(n_string)-1-i)))+1))
            curent = int(n_string[0:i + 1])
    return count
print(count_of2s_in_range(22))
        
    
        
=======
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
    
        
>>>>>>> 2c0ca53018d08ae14a21a7692dbfc9ed498fb7ee
    
#Narek
#1
def asc_order(a):
    c = 0
    for i in range(len(a) - 1):
        if a[i] >= a[i+1]:
            c += a[i] - a[i + 1] + 1 
            a[i+1] = a[i] + 1
    return c
print(asc_order([1,1,1]))

##2
def al(a):
    c = 0
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            c +=1      
    return c <= 1
print(al([5,4,6,9,3]))

#Ruben
#1
n = int(input())
a = [[input(),float(input())] for i in range(n)]
second = sorted(list(set([elem[1] for elem in a])))[1]
b = [el[0] for el in a if second == el[1]]
for elem in sorted(b):
    print(elem)
#2
superString = "abcdefghijklmnop"
subString = "dafebcj"
start = 0
end = 0
for sub in range(len(subString)):
    for sup in range(len(superString)):
        if subString[sub] == superString[sup]:
            if start < sup:
                start = sup
            elif end < sup:
                end = sup
            break
print(superString[start:end + 1])
        

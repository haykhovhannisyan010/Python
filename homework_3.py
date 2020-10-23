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

#2
def al(a):
    a.insert(0,min(a)-1)
    c = 0
    for i in range(2,len(a)):
        if a[i] <= a[i - 1] and a[i] > a[i - 2]:
            c += 1
            a[i-1] = a[i]
        elif a[i] <= a[i - 1] and a[i] <= a[i -2]:
            c += 1
            a[i]=a[i-1]
    return c <= 1 
print(al([1,2,1,2]))

#Ruben
#1
a = [[input(),float(input())] for _ in range(int(input()))]
second = sorted(list(set([elem[1] for elem in a])))[1]
b = [el[0] for el in a if second == el[1]]
for elem in sorted(b):
    print(elem)

#2
def describe_the_str(string):
    dict_ = {}
    for symb in set(string):
        dict_[symb] = string.count(symb)
    return dict_

def dict_contains(dict_1,dict_2):
    for key in dict_2:
        if dict_1.get(key,0) < dict_2[key]:
            return False
    return True
def min_len_sub(superString,subString):
    super_length = len(superString)
    sub_length = len(subString)
    desc_of_subString = describe_the_str(subString)
    t = 0
    while sub_length + t <= super_length :
        start,end = 0 ,sub_length + t
        while end <= super_length and not dict_contains(describe_the_str(superString[start:end]),desc_of_subString):
            start += 1
            end += 1
        if dict_contains(describe_the_str(superString[start:end]),desc_of_subString):
            return (superString[start:end])
        elif end > super_length:
            t+= 1
    return "The SuperString doesn't contain the Substring"       
superString = input("Input the superstring : ")
subString = input("Input the substring : ")
print(min_len_sub(superString,subString))
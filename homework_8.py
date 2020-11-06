##Narek
##1

##2
def l_m(l):
    l.sort(reverse = True)
    return l[0] * l[1] * l[2]
print(l_m([9, 5, 8, 5, 20, 1, 2, -3, -2, -1, 0]))

#Ruben 
#1
def answer_queries(k, *q):
    q = list(q)
    c = 1
    if len(q) < 2:
        if k < q[0]:
            return (q[0] // k + 1)
    else:
        if k > q[0]:
            return 1
        else:
            return(sum(q) // k + 1)
        
print(answer_queries(3,100))

#2
def non_decreasing_sequence(*nums):
    l = list(nums)
    if l == sorted(l,reverse = True):
        return "Yes"
    else:
        for i in range(len(l)):
            for j in range(len(l)):
                l[i] = -l[i]
                l[j] = -l[j]
                if l == sorted(l):
                    return 'Yes'
                else:
                    l[i] = -l[i]
                    l[j] = -l[j]
        return 'No'
print(non_decreasing_sequence(7,4,3,-2))



#def non_decreasing_sequence(*nums):
    #list1 = list(nums)
    #for i in range(len(list1)):
        #list1[i] = 0 - list1[i]
        #if list1 == sorted(list1):
            #return 'Yes'
        #else:
            #list1[i] = 0 - list1[i]
    #for i in range(len(list1)):
        #for j in range(len(list1)):
            #list1[i] = 0 - list1[i]
            #list1[j] = 0 - list1[j]
            #if list1 == sorted(list1):
                #return 'Yes'
            #else:
                #list1[i] = 0 - list1[i]
                #list1[j] = 0 - list1[j]
    #return 'No'


#print(non_decreasing_sequence(7,4,3,2))
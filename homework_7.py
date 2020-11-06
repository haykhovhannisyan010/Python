##Narek
##1
#l = [2,4, -5, 7, 8, 3]
#a = []
#b = []
#for i in range(len(l)):
    #if l[i] > 0:
        #a.append(l[i])
    #else:
        #b.append(l[i])
#a.sort()
#x = 0
#for i in range(len(a) + len(b)):
    #if l[i] > 0:
        #l[i] = a[x]
        #x+=1    
#print(l)
    
##Ruben
##1 
#l = [1,4,6,5,7,10]
#a = []
#b = []
#def swap_list_elements(l):
    #x = 0
    #y = 0    
    #for i in range(len(l)):
        #if l[i] % 2 == 0:
            #a.append(l[i])
        #else:
            #b.append(l[i])
    #for i in range(len(a) + len(b)):
        #if i % 2 == 0:
            #l[i] = a[x]
            #x += 1
        #else:
            #l[i] = b[y]
            #y += 1
    #return l
#print(swap_list_elements([1,4,6,5,7,10]))
    
##2
#import random
#a = []
#b = []
#def get_count_rectangles(d):
    #for _ in range(len(d) * 50):
        #s = random.sample(d.keys(),4)
        #a.append(s)
    #for elem in a:
        #first = d[elem[0]]
        #second = d[elem[1]]
        #third = d[elem[2]]
        #four =  d[elem[3]]
        #if first[0] == second[0] and second[1] == third[1] and third[0] == four[0]\
        #and first[1] == four[1]:
            #b.append("".join(sorted(list(elem))))  
    #return(set(b))
#d= {'A': (0, 0), 'B': (0, 4), 'C': (2, 0), 'D': (2, 4), 'E': (0, -4), 'F': (2, -4)}
#print(get_count_rectangles(d))


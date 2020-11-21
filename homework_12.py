#Narek
#1
def numstriangle(n):
    c = 1
    stop = 2
    for i in range(n):
        for j in range(1, stop):
            if c-1 != n:
                print(c, end=' ')
                c += 1
            else:
                break
        if c-1 != n:
            print()
        stop += 1
numstriangle(9)

#2
def luckynum(a):
    for elem in enumerate(a):
        if elem[0] == elem[1]:
            return elem[0]
    return -1
print(luckynum([-1,0,1,4]))



#Ruben
1
def newRoadSystem(roadRegister):
    to_city = roadRegister
    from_city = list(zip(*roadRegister))
    for i in range(len(roadRegister)):
        if to_city[i].count(True) != from_city[i].count(True):
            return False
    return True

print(newRoadSystem([[False,True,False,False], 
                     [False,False,True,False], 
                     [True,False,False,True], 
                     [False,False,True,False]]))



#2
def efficientRoadNetwork(n, roads):
    a = [[] for i in range(n)]
    for el in roads:
        a[el[0]].append(el[1])
        a[el[1]].append(el[0])
    for i in range(n - 1):
        x = {c for c in a[i]}
        y = {c for c1 in x for c in a[c1]}
        if len({i} |  x  | y) < n:
            return False
    return True

print(efficientRoadNetwork(6,[[3,0], 
                              [0,4], 
                              [5,0], 
                              [2,1], 
                              [1,4], 
                              [2,3], 
                              [5,2]]))

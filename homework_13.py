#Narek
#1
def equalwords(word1,word2):
  return sorted(word1) == sorted(word2)

print(equalwords("abvdj","vjdab"))


#2
def findelem(matrix,elem):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == elem:
                return i,j
    return -1
print(findelem([[10,20,30,40],
                [15,25,35,45],
                [27,29,37,48],
                [32,33,39,50]],25))
            
            
#Ruben 
#1
def financialCrisis(roadRegister):
    a = []
    for i in range(len(roadRegister)):
        b = []
        for j in range(len(roadRegister)):
            row = []
            if j != i:
                for k in range(len(roadRegister[0])):
                    if k != i:
                        row.append(roadRegister[j][k])
                b.append(row)
        a.append(b)
    return a


#2
def namingRoads(roads):
    d = {el[2]: el[:2] for el in roads}
    for i in range(len(roads)):
        if i+1 < len(roads):
            for elem in d[i]:
                if elem in d[i+1]:
                    return False
    return True
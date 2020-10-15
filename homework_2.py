##1 
#n = input()
#nums = []
#d = {}
#while n != "End":
    #nums.append(n)
    #n = input()
#for m in nums:
    #if m in d:
        #continue
    #else:
        #d[int(m)] = nums.count(m)
#print(d)

##2 
#for row in range(1,5):
    #for i in range(1,row+1):
        #print(row, end=" ")  
    #print(" ")
    
    
#1
for i in range(100):
    for j in range(100):
        if i ** j == j**i and i!= j:
            print(i,j,i**j, )
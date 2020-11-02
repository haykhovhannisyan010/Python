#Overall
d = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
def get_value(val): 
    for key, value in d.items(): 
        if val == key: 
            return value
def get_key(val): 
    for key, value in d.items(): 
        if val == value: 
            return key
#Narek
#1
l1,n1 = input()
l2,n2 = input()
def chess_board_color(l1, n1, l2, n2):
    if((int(get_value(l1)) + int(n1)) % 2 == (int(get_value(l2)) + int(n2)) %  2 ):
        return True
    else:
        return False    
print(chess_board_color(l1, n1, l2, n2))
#2
board = [  
    [0, 0, 0, "r", 0, 0, 0,0],        
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],    
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, "q", 0, 0, 0, 0, 0],
    ["ek", "r", 0, 0, 0, 0, 0, 0,],
 ]
k = True
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'ek':
            ek = [i+1,j+1]
        elif board[i][j] == 'q':
            q = [i+1,j+1]
        elif board[i][j] == 'r':
            if k == True:
                r1 = [i+1,j+1]
                k = False
            else:
                r2 = [i+1,j+1]
a = 0
if (r1[0] == ek[0] or r1[1] == ek[1]) or (r2[0] == ek[0] or r2[1] == ek[1])\
or (abs(q[0] - ek[0]) <= 1 and abs(q[1] - ek[1]) <= 1) \
or q[0] == ek[0] or q[1] == ek[1] :
    for i in range(ek[0] - 1,ek[0] + 2):
        if a == 1:
            break
        for j in range(ek[1] - 1,ek[1] + 2):
            if i > 0 and i < 9 and j > 0 and j < 9:
                if not (r1[0] == i or r1[1] == j or r2[0] == i or r2[1] == j \
                or q[0] == i or q[1] == j or abs(q[0] - i) == abs(q[1] - j)):
                    k =  False
                    a = 1
                    break        
            else:
                continue
    for i in range(ek[0] - 1,ek[0] + 2):
        for j in range(ek[1] - 1,ek[1] + 2):
            if q == [i , j] :
                if i == r1[0] or j == r1[1] or i== r2[0] or j == r2[1]:
                    print(True)
                    print([i,j])
                else:
                    print(False)
            elif r2 == [i,j]:
                if i == r1[0] or j == r1[1] or i == q[0] or j == q[1] \
                or abs(q[0] - i) == abs(q[1] - j):
                    print(True)
                else:
                    print(False)
            elif r1 == [i,j]:
                if i == r2[0] or j == r2[1] or i == q[0] or j == q[1] \
                or abs(q[0] - i) == abs(q[1] - j):
                    print(True)
                else:
                    print(False)
else:
    print(False)   
#Ruben
#1
n1,l1 = input()
l = []
def possible_turns(n1,l1):
    for i in range(1,9):
        for j in range(1,9):
            x = abs(int(get_value(n1))-i)
            y = abs(int(l1) - j)
            if x == 1 and y == 2 or x == 2 and y == 1:
                l.append([get_key(i),j])
    return l
possible_turns(n1,l1)
a = []
for elem in l:
    elem[1] = str(elem[1])
    a.append("".join(elem))
print(a)

#2
chess_board = [  
    [0, 0, 0, 0, 0, 0, 0,0],        
    [0, 0, "q", 0, 0, 1, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],    
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0,],
 ]
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        if chess_board[i][j] == 'q':
            q = [i+1,j+1]
flag = False
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):
        if i == q[0] - 1 and chess_board[i][j] != "q":
            if chess_board[i][j] == 1:
                flag = True
            if flag:
                break
            else:
                chess_board[i][j] = "x"
flag = False                
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):                
        if j == q[1] - 1 and chess_board[i][j] != "q":
            if chess_board[i][j] == 1:
                flag = True
            if flag:
                break
            else:
                chess_board[i][j] = "x"            
flag = False                
for i in range(len(chess_board)):
    for j in range(len(chess_board[i])):                
        if abs(q[0] - 1 - i) == abs(q[1] - 1 - j) and chess_board[i][j] != "q":
            if chess_board[i][j] == 1:
                flag = True
            if flag:
                break
            else:
                chess_board[i][j] = "x" 
print(chess_board[0])
print(chess_board[1])
print(chess_board[2])
print(chess_board[3])
print(chess_board[4])
print(chess_board[5])
print(chess_board[6])
<<<<<<< HEAD
print(chess_board[7])
=======
print(chess_board[7])
>>>>>>> be04ed91ce1ba786f17355f8ea27fc2f0a0d49f7

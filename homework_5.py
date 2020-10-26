#Narek
#1
a = [1,5,20,30]
list_ = []
flag = False
for j in range(3,int(max(a)-1)):
    list_2 = []
    for i in range(1,len(a)):
        rem = a[1] % j
        if a[i] % j == rem :
            list_2.append(a[i])
            if len(a)-1 == len(list_2):
                flag = True
                break
    if flag:
        list_.append(a[0])
        list_.append(a[1])
        for k in range(1,max(a)):
            if list_[k] > max(a)-1:
                break
            list_.append(list_[k] + j)
        break      
if list_:
    print(flag,list_)
else:
    print(flag)
#2
def check_winner(board):
    if "Empty" in board[0] or "Empty" in board[1] or "Empty" in board[2] :
        x = []
        o = []
        for i in board:
            for j in i:
                if j == "x":
                    x.append(j)
                elif j == "o":
                    o.append(j)
        if len(x) > len(o):
            return "O's turn"
        else:
            return "x's turn"
    else:
        winner = ""
        for row in range(0,3):
            if board[row][0]==board[row][1]==board[row][2]=="x":
                winner = "x is winner"
            elif board[row][0]==board[row][1]==board[row][2]=="o":
                winner = "o is winner"
        for col in range(0,3):
            if board[0][col]==board[1][col]==board[2][col]=="x":
                winner = "x is winner"
            elif board[0][col]==board[1][col]==board[2][col]=="o":   
                winner = "o is winner"
        if board[0][0]==board[1][1]==board[2][2]=="x":
            winner = ('x is winner')
        elif board[0][0]==board[1][1]==board[2][2]=="o":
            winner = "o is winner"
        if board[0][2]==board[1][1]==board[2][0]=="x":
            winner = "x is winner"
        elif board[0][2]==board[1][1]==board[2][0]=="o":
            winner = "x is winner"
        if winner == "":
            return -1
        else:
            return winner
        
print(check_winner([["x","o","x"],
                   ["o","x","o"],
                   ["x","x","o"]]
                  ))
##Ruben
#1
name = []
gr = input()
for i in range(len(gr.split(", "))):
    anun = input().split(",")
    name.append((anun))
stug = input().split(", ")
gr1,gr2 = gr.split(", ")
l = []
for i in range(len(name)):
    for j in range(len(name) + i):
        l.append(name[i][j])
b = []
for i in l:
    for j in stug:
        if j == i:
            b.append(j)
for i in range(len(b)-1):
    if b[i-1] == b[0]:
        b.remove(b[i])
x = 0
y = ""
if sorted(b)[0] in name[0]:
    x = str(len(name[0]))
elif sorted(b) in an[1]:
    x = str(len(name[1]))
if x in gr1.split(": "):
    y = gr1.split(": ")[0]
elif x in gr2.split(": "):
    y = gr2.split(":")[0]
print(b[0],": ",y)

#matem: 3, yandex: 2
#ivanov,petrov
#ivanov,aleqs,sidorov
#ivanov, petrov
                 
                  
##2              
list_ = []
count = 1
amount = 0
def add_item(itemName,itemCost):
    global list_,count
    list_.append([itemName,itemCost])
    return list_

def print_receipt():
    global count,amount,list_
    if len(list_) == 0:
        return
    print('Check {} Number of items: {}'.format(count,len(list_)))
    for i in range(len(list_)):
        amount += list_[i][1]
        print('{} - {}'.format(list_[i][0], list_[i][1]))
    count += 1
    print('Total: ' + str(amount))
    print('-' * 5)
    amount = 0
    list_ = []
add_item("bloknot" , 100)
add_item("grich",10)
print_receipt()
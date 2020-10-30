#Narek
#1
#a = [1,5,20,30]
#list_ = []
#flag = False
#for j in range(3,int(max(a)-1)):
    #list_2 = []
    #for i in range(1,len(a)):
        #rem = a[1] % j
        #if a[i] % j == rem :
            #list_2.append(a[i])
            #if len(a)-1 == len(list_2):
                #flag = True
                #break
    #if flag:
        #list_.append(a[0])
        #list_.append(a[1])
        #for k in range(1,max(a)):
            #if list_[k] > max(a)-1:
                #break
            #list_.append(list_[k] + j)
        #break      
#if list_:
    #print(flag,list_)
#else:
    #print(flag)
      
##2.1
#def tictactoe(board):
    #x_y_cord = []
    #o_y_cord = []
    #x1_count = 0
    #x2_count = 0 
    #o1_count = 0
    #o2_count = 0     
    #count = 0
    
    #for i in range(len(board)):
        #for j in range(len(board[i])):
            #if board[i][j] == "x":
                #x_y_cord.append(j)
                #count += 1
                #if board[i].count("x")==len(board) or x_y_cord.count(j) == len(board):
                    #return "x"
                #if i == j:
                    #x1_count += 1
                #if i+j==2:
                    #x2_count += 1
            #elif board[i][j] == "o":
                #o_y_cord.append(j)
                #count += 1
                #if board[i].count("o")==len(board) or o_y_cord.count(j) == len(board):
                    #return "o"
                #if i == j:
                    #o1_count += 1
                #if i+j==2:
                    #o2_count += 1   
    #if x1_count==len(board) or x2_count == len(board):
        #return "x"
    #elif o1_count==len(board) or o2_count == len(board):
        #return "o"
    #if count < 9 and count%2== 0:
        #return "x's turn"
    #elif count<9 and count %2 == 1:
        #return "o's turn"
    #return -1
#print(tictactoe([["x","o","x"],
                   #["o","o","o"],
                   #["x","x","o"]]
                  #))          

##2.2
#def check_winner(board):
    #if "Empty" in board[0] or "Empty" in board[1] or "Empty" in board[2] :
        #x = []
        #o = []
        #for i in board:
            #for j in i:
                #if j == "x":
                    #x.append(j)
                #elif j == "o":
                    #o.append(j)
        #if len(x) > len(o):
            #return "O's turn"
        #else:
            #return "x's turn"
    #else:
        #winner = ""
        #for row in range(0,3):
            #if board[row][0]==board[row][1]==board[row][2]=="x":
                #winner = "x is winner"
            #elif board[row][0]==board[row][1]==board[row][2]=="o":
                #winner = "o is winner"
        #for col in range(0,3):
            #if board[0][col]==board[1][col]==board[2][col]=="x":
                #winner = "x is winner"
            #elif board[0][col]==board[1][col]==board[2][col]=="o":   
                #winner = "o is winner"
        #if board[0][0]==board[1][1]==board[2][2]=="x":
            #winner = ('x is winner')
        #elif board[0][0]==board[1][1]==board[2][2]=="o":
            #winner = "o is winner"
        #if board[0][2]==board[1][1]==board[2][0]=="x":
            #winner = "x is winner"
        #elif board[0][2]==board[1][1]==board[2][0]=="o":
            #winner = "x is winner"
        #if winner == "":
            #return -1
        #else:
            #return winner
        
#print(check_winner([["x","o","x"],
                   #["o","x","o"],
                   #["x","x","o"]]
                  #))
###Ruben
##1.1
#name = []
#gr = input()
#for i in range(len(gr.split(", "))):
    #anun = input().split(",")
    #name.append((anun))
#stug = input().split(", ")
#gr1,gr2 = gr.split(", ")
#l = []
#for i in range(len(name)):
    #for j in range(len(name) + i):
        #l.append(name[i][j])
#b = []
#for i in l:
    #for j in stug:
        #if j == i:
            #b.append(j)
#for i in range(len(b)-1):
    #if b[i-1] == b[0]:
        #b.remove(b[i])
#x = 0
#y = ""
#if sorted(b)[0] in name[0]:
    #x = str(len(name[0]))
#elif sorted(b) in an[1]:
    #x = str(len(name[1]))
#if x in gr1.split(": "):
    #y = gr1.split(": ")[0]
#elif x in gr2.split(": "):
    #y = gr2.split(":")[0]
#print(b[0],": ",y)

##matem: 3, yandex: 2
##ivanov,petrov
##ivanov,aleqs,sidorov
##ivanov, petrov
                 
##1.2
import math
groups = input().split(", ")
group_counts = {}
for group in groups:
    group_name, group_count = tuple(group.split(": "))
    group_counts[group_name] = group_count
for _ in range(len(groups)):
    students = input().split(", ")
    for group_name in group_counts:
        if group_counts[group_name] == len(students):
            group_students[group_name] == students
names_to_compare
student_group = {}
for group_name in group_students:
    for student in group_students[group_name]:
        if student_group.get(student,None) is not None:
            students_group[student].append(group_name)
        else:
            student_group[student] = [group_name]
min_value = math.inf
for student in student_group:
    if len(student_group[student]) < min_value:
        min_value = len(student_group)
min_student_list = []
for student in student_group:
    if len(student_group[student]) == min_value and student in names_to_compare:
        min_student_list.append(student)
min_student = sorted(min_student_list)[0]
print(f"{min_student}: {'.'.join(student_group[min_student])}")
        
    
            
###2              
#list_ = []
#count = 1
#amount = 0
#def add_item(itemName,itemCost):
    #global list_,count
    #list_.append([itemName,itemCost])
    #return list_

#def print_receipt():
    #global count,amount,list_
    #if len(list_) == 0:
        #return
    #print('Check {} Number of items: {}'.format(count,len(list_)))
    #for i in range(len(list_)):
        #amount += list_[i][1]
        #print('{} - {}'.format(list_[i][0], list_[i][1]))
    #count += 1
    #print('Total: ' + str(amount))
    #print('-' * 5)
    #amount = 0
    #list_ = []
#add_item("bloknot" , 100)
#add_item("grich",10)
#print_receipt()  
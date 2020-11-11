
##Narek
##1
#a = [1,4,10,6,2]
#minn = b = 0
#c = []
#for j in range(2,max(a)): 
    #for i in a:
        #if i % j != 0:
            #minn+= 1
            #if minn == len(a):
                #b = j
                #c.append(b)
        #else:
            #minn = 0
            #break
#print(min(c) if c else max(a)+1)
#Narek
#1
a = [2,8,5,3,4,6,7]
minn = b = 0
c = []
for j in range(2,max(a)): 
    for i in a:
        if i % j != 0:
            minn+= 1
            if minn == len(a):
                b = j
                c.append(b)
        else:
            minn = 0
            break
print(min(c) if c else max(a)+1)

               
##2
a = "+4x+50-x=-40"
if a[0].isalnum():
    a = '+' + a
index = 0
list_1 = []
for i in range(1, len(a)):
    if not a[i].isalnum():
        list_1.append(a[index:i])
        index = i
x_value = int(a[a.index('=') + 1:])
x_cofficent = 0
print(list_1)
for i in list_1:
    if i[1:].isdigit():
        if i[0] == "-":
            x_value += int(i[1:])
        else:
            x_value -= int(i[1:])
    else:
        if i[1:i.find('x')].isdigit():
            x_cofficent += int(i[:i.find('x')])
        else:
            if i != "=":
                x_cofficent += int(i[0] + "1")
x_value /= x_cofficent
print(f'x={x_value}')

    
#Ruben
#1
def get_neighbours_coords(i_cord, j_cord, matrix_i, matrix_j):
    coords = []
    for i in range(i_cord - 1, i_cord + 2):
        for j in range(j_cord - 1, j_cord + 2):
            if 0 <= i <= matrix_i - 1 and 0 <= j <= matrix_j - 1 and (i, j) != (i_cord, j_cord):
                coords.append((i, j))
    return coords


def minesweeper(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            neighbours_coords = get_neighbours_coords(i, j, len(matrix), len(matrix[i]))
            count = 0
            for coord_x, coord_y in neighbours_coords:
                if matrix[coord_x][coord_y]:
                    count += 1
            new_matrix[i].append(count)
    return new_matrix
#2
word = input()
t = 1
start, end = 0, 0 + t
vowels = {}
consonants = {}
while t < len(word):
    if word[start] in 'aeyuio':
        vowels[word[start:end]] = vowels.get(word[start:end], 0) + 1
        start += 1
        end += 1
    elif word[start] not in 'aeyuio':
        if word[start] in 'aeiou':
            vowels[word[start:end]] = vowels.get(word[start:end], 0) + 1
            start += 1
            end += 1
        elif word[start] not in 'aeiou':
            consonants[word[start:end]] = consonants.get(word[start:end], 0) + 1
            start += 1
            end += 1
        if end == len(word) + 1:
            t += 1
            start = 0
            end = 0 + t
print(vowels, consonants, sep='\n')


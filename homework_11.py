#Narek
#1
def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
print(countDigit(24))

#2
def sum_elements(ints, summ):
    s = set()
    a = []
    for elem in ints:
        if summ - elem in s:
            a.append(tuple([summ - elem, elem]))
        s.add(elem)
    return a if a else  -1
print(sum_elements([5,2,2,1,3],4))


#Ruben
#1
def rotateImage(a):
    for i in range(len(a) // 2):
        end = len(a) - 1 - i
        for j in range(end - i):
            k = a[i][i+j]
            a[i][i+j] = a[end-j][i]
            a[end-j][i] = a[end][end-j]
            a[end][end-j] = a[i+j][end]
            a[i+j][end] = k
    return a


print(rotateImage([[10,9,6,3,7],
                   [6,10,2,9,7],
                   [7,6,3,8,2],
                   [8,9,7,9,9],
                   [6,8,6,8,2]]))


#2
a = []
def get_digits(product):
    global a
    if product in range(9,1,-1):
        a.append(product)
    else:
        for i in range(9,1,-1):
            if product%i == 0:
                a.append(i)
                break
            if i == 2 and product % i != 0:
                a.append(-1)
                return -1
        return get_digits(product//i)       
    
def digitsProduct(product):
    if product < 10: 
        if product == 0: 
            return 10  
        return product
    get_digits(product)
    if -1 in a:
        return -1
    str_number= ''
    for i in reversed(a):
        str_number+= str(i)
    return int(str_number)
 

print(digitsProduct(7))


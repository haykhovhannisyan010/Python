<<<<<<< HEAD
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
=======
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
>>>>>>> 4bc3c12082bea3fc8e5b113a9c7b5353f801bb67
               
##2
#n = "2x+15-1+2=35"
#c = 0
#for i in range(len(n)):
    #c += 1
    #if n[i] == "=":
        #break
#a = n[:c-1]
#b = [n[c:]]
#h = [n[c:]]
#x = []
#for j in range(len(a)):
    #if not "x" in a[j]:
        #if a[j] == "+":
            #b.append("-")
        #elif a[j] == "-":
            #b.append("+")
        #else:
            #b.append(a[j])
    #else:
        #while h != b:
            #if b[-1] != "+" or b[-1] != "-":
                #x.append(b[-1])
                #b.pop()
                #break
#b = "".join(b)
#x.reverse()
#x = "".join(x)
#if x:
    #print(eval(b) / int(x[0]))
#else:
    #print(eval(b))
    
    
#Ruben
<<<<<<< HEAD
#1
=======
#2
>>>>>>> 4bc3c12082bea3fc8e5b113a9c7b5353f801bb67
word = input()
t = 1
start, end = 0, 0 + t
vowels = {}
consonants = {}
while t < len(word):
<<<<<<< HEAD
    if word[start] in 'aeyuio':
        vowels[word[start:end]] = vowels.get(word[start:end], 0) + 1
        start += 1
        end += 1
    elif word[start] not in 'aeyuio':
=======
    if word[start] in 'aeiou':
        vowels[word[start:end]] = vowels.get(word[start:end], 0) + 1
        start += 1
        end += 1
    elif word[start] not in 'aeiou':
>>>>>>> 4bc3c12082bea3fc8e5b113a9c7b5353f801bb67
        consonants[word[start:end]] = consonants.get(word[start:end], 0) + 1
        start += 1
        end += 1
    if end == len(word) + 1:
        t += 1
        start = 0
        end = 0 + t
<<<<<<< HEAD
print(vowels, consonants, sep='\n')
=======
print(vowels, consonants, sep='\n')
>>>>>>> 4bc3c12082bea3fc8e5b113a9c7b5353f801bb67

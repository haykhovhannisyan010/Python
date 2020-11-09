#Ruben
#1
def buildPalindrome(string):
    b = string[::-1]
    for i in range(len(b),0,-1):
        c = b[i:]
        if string + c == c[::-1] + string[::-1]:
            return (string + c)
print(buildPalindrome("abcd"))

#2
a = set()  
x = 0   
def all_increasing_sequences(k,n,x,l):   
    global a
    if x == n:
        for i in range(n): 
            k = [k for k in l]
            a.add(tuple(k))
    else:
        i = 1 if x == 0 else l[x - 1] + 1
        x += 1    
        while (i <= k): 
            l[x - 1] = i
            all_increasing_sequences(k,n,x,l)
            i += 1
        x -= 1  
        
def all_increasing_sequences_print(n,k): 
    l = [0] * n
    all_increasing_sequences(k, n, x, l)
    return a
        
print(all_increasing_sequences_print(2,8))

#Narek
#1
def get_coin(l):
    a = l
    if l == [1]:
        return b.index(l[0])
    else:
        l = len(l) // 2
        if 1 in a[l:]: 
            return get_coin(a[l:])
        else:
            return get_coin(a[:l])
b = [2,2,2,1,2,2,2,2]      
print(get_coin(b))

#2
def word_rotate(word):
    if "(" in word and ")" in word:
        for i in range(len(word)):
            if word[i] == "(":
                start = i
            elif word[i] == ")":
                end = i
        word_rotate(word[:start] + word[start+1:end][::-1] + word[end+1:])
    else:
        print(word)
        
word_rotate("H(ya)k (oH)vh(nnah)isyan")

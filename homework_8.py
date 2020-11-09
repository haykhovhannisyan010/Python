#Narek
#1      
def get_books_and_date(author,**names):
    d = {}
    for key,value in names.items():
        if value[0] == author:
            d[key] = value[1]
    sorted_d = sorted((value, key) for (key,value) in d.items())
    for i in range(len(sorted_d)):
        print(*sorted_d[i])


get_books_and_date("John", Book_1 =["John",1984], Book_2 =["Bob",1974],\
                Book_3=["Mark",1785],Book_4 =["Markes",1874],\
                Book_5=["John",1858])
    
#2
def l_m(l):
    l = [9, 5, 8, 5, 20, 1, -20, -1, -30] 
    positive = [i for i in l if i > 0]
    negative = [j for j in l if j < 0]
    positive.sort(reverse = True)
    negative.sort()
    if len(negative) > 1:
        if abs(negative[0]) * abs(negative[1]) * positive[0] > positive[0] \
        * positive[1] * positive[2]:
            return (abs(negative[0]) * abs(negative[1]) * positive[0])
        else:
            return (positive[0]  * positive[1] * positive[2]) 
    else:
        return (positive[0]  * positive[1] * positive[2]) 
print(l_m([9, 5, 8, 5, 20, 1, 2, -20, -1, -30]))

#Ruben 
#1
def answer_queries(k, *q):
    c = 1
    l = list(q)
    for i in range(len(l)):
        if i == len(l) - 1:
            if k - l[i] > 0:
                return c
            elif k < l[i]:
                c += (l[i]) // k
                return c            
        else:
            if k - l[i] > 0:
                return c
            elif k < l[i]:
                l[i + 1] += l[i] - k
            c += 1                    
    return c + 1
print(answer_queries(5,6,3,3,3))
#2
import math
def non_decreasing_sequence(*nums):
    nums = list(nums)
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            prev = nums[i - 1] if i - 1 >= 0 else -math.inf
            next = nums[i + 2] if i + 2 < len(nums) else math.inf
            if prev <= nums[i] >= next and prev <= -nums[i] <= next:
                nums[i], nums[i + 1] = -nums[i], -nums[i + 1]
        elif abs(nums[i]) == abs(nums[i + 1]):
            if -nums[i + 1] >= nums[i + 1]:
                nums[i + 1] = -nums[i + 1]
        elif nums[i] > nums[i + 1] and abs(nums[i]) > abs(nums[i + 1]):
            nums[i], nums[i + 1] = -nums[i], -nums[i + 1]
        elif nums[i] > nums[i + 1] and abs(nums[i]) < abs(nums[i + 1]):
            nums[i + 1] = -nums[i + 1]
        i += 1
    if nums == sorted(nums):
        return f"Yes \n{nums}"
    return "No"
print(non_decreasing_sequence(3,2,5))
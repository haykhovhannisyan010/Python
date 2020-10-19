#1
text = input("Enter text - ")
text = text.replace("."," ")
text = text.replace(":"," ")
text = text.replace("!"," ")
text = text.replace("?"," ")
print(text)

#2
nums = [int(n) for n in input()]
print(round(sum(nums)/len(nums),1))

#3 
text = input("Enter text - ").split()
count = 0
for w in text:
    if w[0].isupper():
        count += 1 
print(count)

#4
v_name = input()
if not(v_name[0].isdigit()) and v_name.isalnum() or "_" in v_name:
    print("True")
else:
    print("False")
def rotate(l,n):
    return l[n:]+l[:n]

name1 = str(input("enter your name : ")).replace(" ","")
name2 = str(input("enter your parnter's name : ")).replace(" ","")
print(name1,name2)
temp1 = list(set(name1)-set(name2))
temp2 = list(set(name2)-set(name1))
count = len(temp1) + len(temp2)
print(count)
flames = 'flames'
flames = list(flames)
while len(flames) != 1:
    for i in range(0,count):
        flames=rotate(flames,1)
        #print(flames)
    temp = len(flames) - 1
    flames.pop(temp)
    print(flames)
#print(flames)

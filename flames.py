def rotate(l,n):
    return l[n:]+l[:n]
flamesdict = {'f':'Friends','l':'Lovers','a':'Acquaintances','m':'Marriage','e':'Enemies','s':'Siblings'}
name1 = str(input("enter your name : ")).replace(" ","")
name2 = str(input("enter your parnter's name : ")).replace(" ","")
temp1 = list(set(name1)-set(name2))
temp2 = list(set(name2)-set(name1))
count = len(temp1) + len(temp2)
flames = 'flames'
flames = list(flames)
while len(flames) != 1:
    for i in range(0,count):
        flames=rotate(flames,1)
    temp = len(flames) - 1
    flames.pop(temp)
print('You both are related by : ',flamesdict[flames[0]])

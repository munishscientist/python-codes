list=[]
print hello 
num=input("Enter the number :")
num=int(num)
a=0
b=1
for x in range(num):
    c=a+b
    list.append(c)
    a=b
    b=c
print(list)
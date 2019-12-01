n=int(input())
list=[]
print("enter the list :")
b=0
c=0
for x in range(0,n): 
   p=int(input())
   list.append(p)
  
for x in range(0,n):
    b=c+list[x]
    c=b
    
if(c%2==0 and c%3==0 and c%5==0):
   print(1)
else:
   print(0)
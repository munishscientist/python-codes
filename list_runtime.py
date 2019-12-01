n=int(input("enter element "))
lis=list(map(str,input("elements ").strip().split()))
#print(lis)
count=0
v=[]
q=[]

for x in range(0,10) :
  
    c=lis[x]
    
    V=lis.count(c)
    
    if V>=2 :
     #  for x in v:
       v.append(c)
          
f=v[V-1]
q.append(f)
print("output ")      
print(q)    
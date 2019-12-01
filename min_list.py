n=int(input())
lis=list(map(int,input().strip().split()))[:n]
v=[]
g=[]
for x in range(0,n):
    c=lis[x] 
    g=lis.index(lis[x])
    if c==4:   
       v.append(g)
      
print(max(v))
print(v)

p=lis.index(lis[4])
print(p)
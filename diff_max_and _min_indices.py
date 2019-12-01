n=int(input())
lis=list(map(int, input().strip().split()))[:n]
b=max(lis)
c=min(lis)

e=lis.index(b)
f=lis.index(c)

print(e-f)
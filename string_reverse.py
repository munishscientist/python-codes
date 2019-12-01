num=int(input())
count=0
for x in range(num):
   num=str(num)
   rev=num.reverse(num)
   
   if(num==rev): 
      count=count+1
print("the number of palindrome is : ",count)
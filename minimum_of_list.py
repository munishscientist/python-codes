Num=int(input.split("Enter the number of element"))
list=[]
for x in range (Num):
    print("Enter the element : ",x)
    value=input()
    list.append(value)
    
print(min(list))

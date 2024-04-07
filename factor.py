#find the factor of the number
num=int(input("enter the number:"))
print("the factor of ",num,"is:")
for i in range(1,num+1):
    if(num%i==0):
        print(i)
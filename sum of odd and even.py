even=0
odd=0
n=eval(input("enter the number:"))
for i in range(1,n+1,1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print("sum of even :",even)
print("sum of odd :",odd)

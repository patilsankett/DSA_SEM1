num=int(input("Enter the Num :"))
p=len(str(num))
n=num
sum=0

while (num>0):
    sum += (num%10)**p                  
    num //=10
if(n==sum):
    print("Num is Armsrtrong")
else:
    print("Num is not Armstrong")

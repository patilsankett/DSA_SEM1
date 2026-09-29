num=int(input("Enter the num :"))
sum=0
n=num

while(num>0):
    rem=num%10
    sum=sum*10+rem
    num //=10
if(n==sum):
    print("Num is Palindrome !!")
else:
    print("Not palindrom")

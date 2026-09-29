num=int(input("Enter the Number :"))
flag=0
for i in range(2,(num//2)+1):
    if(num % i==0):
        flag = 1
        break
if (flag==1):
        print("Not Prime")
else:
        print("The Num is Prime")
n=int(input("Enter the number :"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the num :")))

even = 0
odd = 0
for i in range(n):
    if arr[i]%2 == 0:
        print(even)
        even +=1
    else:
        odd +=1
print("Even elemests :", even)
print(f"odd elements ={odd}")

n = int(input("Enter Number: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter integer: ")))
arr.sort()
print("Array =",arr)
print("Smallest element =",arr[0])
print("Second smallest element =",arr[1])
print("Largest element =",arr[n-1])
print("Second largest element =",arr[n-2])
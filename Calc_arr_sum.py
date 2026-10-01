n = int(input("Enter Number : "))
arr = []

for i in range(n):
    arr.append(int(input("Enter integer: ")))

total = 0
for i in range(n):
    total += arr[i]

print("Sum =", total)
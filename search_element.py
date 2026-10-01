n = int(input("Enter the number: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter the num: ")))

search = int(input("Enter number to search: "))
found = False
for i in range(n):
    if arr[i] == search:
        print("Number is present at position", i + 1)
        found = True
if found == False:
    print("Number is not present in the array")
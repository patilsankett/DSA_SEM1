arr = [3,45,2,10,20,30,40,50,55]
min = arr[0]
max = arr[0]
sec_min = arr[0]
sec_max = arr[0]

for num in arr:
    if (num < min):
        sec_min = min
        min = num
    if (num > max):
        sec_max = max
        max = num
print("Min Num =",min)
print("Max Num =",max)
print("Sec Min Num =",sec_min)
print("sec Max Num =",sec_max)
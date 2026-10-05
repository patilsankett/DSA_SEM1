#Alphabet Patterns
# n = int(input("Enter no of rows"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end="")
#     print()


# n = int(input("Enter no of rows"))
# num = 0
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+num),end="")
#         num += 1
#     print()
 

#Alphabet Pyramid
n = int(input("Enter no of Rows :"))
for i in range(n):
    print("  "*(n-i+1),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
    print()
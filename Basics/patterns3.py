##11
# n = int(input("enter number of rows: "))
# for i in range(1, n+1):
#     if i % 2 == 1:
#         for j in range(1, i+1):
#             bit = j % 2
#             if bit == 0:
#                 print("0", end=" ")
#             else:
#                 print("1", end=" ")
#         print()
#     else:
#         for j in range(1, i+1):
#             bit = j % 2
#             if bit == 0:
#                 print("1", end=" ")
#             else:
#                 print("0", end=" ")
#         print()

##12
# n = int(input("enter number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print(" " * (2*n - 2*i), end="")
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

##13
# n = int(input("enter number of rows: "))
# start = 1
# for i in range(n):
#     for j in range(i+1):
#         print(start, end=" ")
#         start = start + 1
#     print()

##14
# n = int(input("enter number of rows: "))
# for i in range(n):
#     for j in range(1,i+2):
#         alphabet = chr(j + 64)
#         print(alphabet, end="")
#     print()

##15
# n = int(input("enter number of rows: "))
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         alphabet = chr(j + 64)
#         print(alphabet, end="")
#     print()

##16
# n = int(input("enter number of rows: "))
# for i in range(n):
#     alphabet = chr(i + 65)
#     print(alphabet * (i+1))

##17
n = int(input("enter number of rows: "))
for i in range(n):
    space = n - i
    print(" " * space, end="")
    for j in range(i+1):
        alphabet = chr(j + 65)
        print(alphabet, end="")
    for j in range(i, 0, -1):
        alphabet = chr(j + 65 - 1)
        print(alphabet, end="")
    print()

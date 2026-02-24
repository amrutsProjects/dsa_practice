##1
# n = int(input("enter number: "))
# for i in range (n):
#     print("*" * n)

##2
# n = int(input("enter number of rows: "))
# for i in range (n):
#     print("*" * (i+1))

##3
# n = int(input("enter number of rows: "))
# for i in range (2,n+2):
#     for j in range (1,i):
#         if i - 1 == j:
#             print(j)
#         else:
#             print(j, end="")

##4
# n = int(input("enter number of rows: "))
# for i in range(1, n + 1):
#     for j in range(i+1):
#         if j == i:
#             print(i)
#         else:
#             print(i, end="")

##5
# n = int(input("enter number of rows: "))
# for i in range(n, 0, -1):
#     print("*" * i)

##6
n = int(input("enter number of rows: "))
for i in range(n+1, 0, -1):
    for j in range(1,i):
        if j == i-1:
            print(j)
        else:
            print(j, end="")
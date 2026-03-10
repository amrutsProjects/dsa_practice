import math;
##18
# n = int(input("enter number of rows: "))
# for i in range(n , 0 , -1):
#     for j in range(i, n+1):
#         alphabet = chr(j + 64)
#         print(alphabet, end=" ")
#     print()

##19
# n = int(input("enter number of rows: "))
# for i in range(n):
#     star = n - i
#     space = 2 * i
#     print("*" * star, end="")
#     print(" " * space, end="")
#     print("*" * star)
# for j in range(1, n+1):
#     star = j
#     space = 2*n - 2*j
#     print("*" * star, end="")
#     print(" " * space, end="")
#     print("*" * star)

##20
# n = int(input("enter number of rows: "))
# for j in range(1, n+1):
#     star = j
#     space = 2*n - 2*j
#     print("*" * star, end="")
#     print(" " * space, end="")
#     print("*" * star)
# for i in range(1, n):
#     star = n - i
#     space = 2 * i
#     print("*" * star, end="")
#     print(" " * space, end="")
#     print("*" * star)

##21
# n = int(input("Enter number of rows: "))
# half_of_n =  math.ceil(n/2)
# for i in range(n):
#     if(i == 0 or i == n-1):
#         print("*" * n)
#     else:
#         print("*" + " " * (half_of_n) + "*")
    
##22
n = int(input("Enter number of rows: "))

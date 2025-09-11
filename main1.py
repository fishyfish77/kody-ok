# a=float(input())
# b=float(input())
# c=float(input())
# if a+b>c
#     if c+b>a
#         if c+a>b
#             print("tak")
#         else:
#             print("nie")
#     else:
#         print("nie")
# else:
#     print("nie")        

a=float(input())
b=float(input())
c=float(input())
if a+b>c and c+b>a and c+a>b:
    print("tak")
else:
    print("nie")

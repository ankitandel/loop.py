# i=1
# while i<5:
#     k=1
#     while k<=5-i:
#         print("",end=" ")
#         k=k+1
#     j=i
#     while j>=i-1:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1

r=5
i=r-1
while i>=0:
    j=0
    while j<i:
        print("",end=" ")
        j=j+1
    k=i
    while k<=r-1:
        print("*",end=" ")
        k=k+1
    print("")
    i=i-1


num=int(input("enter the number"))
a=65
i=0
while i<num:
    j=1
    while j<=5:
        b=chr(a)
        print(" ",b,end=" ")
        j=j+1
        a=a+1
    print()
    i=i+1
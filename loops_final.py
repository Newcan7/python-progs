n =int(input("Enter number of lines"))
a=int((n/2)+1)
b=n-a
for i in range(0,a):
    for k in range(a-1,0-1,-1):
        print(" ",end="")
    for j in range(0,(i*2)+1):
        print("  *  ",end="")
    print("\n")
for i in range(b,-1,-1):
    for k in range(b-1,-1,-1):
        print(" ",end="")
    for j in range(0,(i*2)+1):
        print("  *  ",end="")
    print("\n")
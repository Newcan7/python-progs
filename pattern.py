n=int(input("enter number of lines"))
for i in range(0,n):
    for k in range(0,n-i):
        print(" ", end="")
    for j in range(0,i*2+1):
        print("*",end="")
    print("\n")
    
    
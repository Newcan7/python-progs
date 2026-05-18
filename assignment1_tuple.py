d={}
n=int(input("Enter number of students"))
for i in range(1,n+1):
    name=input("Enter name of student:")
    m1=input("Enter maths marks")
    m2=input("Enter science marks")
    m3=input("Enter history marks")
    d[name]=(m1,m2,m3)

print(d)
n=int(input("Enter Number of students: "))
l={}
for i in range(n+1):
    name=input("Enter name", i+1)
    sub1=int(input("Enter marks of sub 1"))
    sub2=int(input("Enter marks of sub 2"))
    l["name"]=(sub1,sub2)
def calc_total(a):
    return (a["sub1"]+a["sub2"])
unique=()
for i in range(n+1):
    unique.add(calc_total(i))

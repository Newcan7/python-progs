n=int(input("Enter Number of students"))
l=[]
for i in range(1,n+1):
    name=input(f"Enter name of student {i}")
    pm=input(f"Enter pm of student{i}")
    cm=input(f"Enter cm of student{i}")
    bm=input(f"Enter bm of student{i}")
    d={"name":name,"physics_marks":pm,"chemistry_marks":cm,"biology_marks":bm}
    l.append(d)

def avg(l):
    a= (l["chemistry_marks"]+l["physics_marks"]+l["biology_marks"])/3
    return a >70

final=list(filter(avg,l))
print(final)

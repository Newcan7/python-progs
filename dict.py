d={}
names_list=[]
total_marks_list=[]
n=int(input("enter number of students"))

for i in range(n):
    name =input("enter name ")
    a=int(input("enter marks in sub1"))
    b=int(input("enter marks in sub2"))
    c=int(input("enter marks in sub3"))
    d[name]=(a,b,c)
    names_list.append(name)
    total_marks_list.append((a+c+b)/3)

for i in range(len(total_marks_list)):
    if total_marks_list.count(total_marks_list[i]) == 1:
        print("name --> ", names_list[i])
        print("marks --> ", d[names_list[i]])






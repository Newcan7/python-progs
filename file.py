# n=input("Enter Filename : ")
ss=""
l=[]
with open("hello.txt",'r') as f:
    for x in f:
        s=x.split()
        for i in s:
            j=i.capitalize()
            l.append(j)
print(l)
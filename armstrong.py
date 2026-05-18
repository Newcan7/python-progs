n=int(input("Enter a number to check: "))
s=0
for i in str(n):
    s=s+int(i)**len(str(n))
if n==s:
    print("Armstrong")
else:
    print("Not Armstrong")
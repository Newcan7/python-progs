p = input("Enter your Password : ")
count=0
if len(p.strip())>=8:
    count+=1
for i in p:
    if i.isupper():
        count+=1
        break;
for i in p:
    if i.islower():
        count+=1
        break;
for i in p:
    if i.isdigit():
        count+=1
        break;
for i in p:
    if i in "!@#$%^&*":
        count+=1
        break;
print(count)





names=[]
for i in range(0,10):
    names.append(input("enter name"))
names_filtered=list(filter(lambda x: x[-1].lower() in "aeiou",names))

print(names_filtered)

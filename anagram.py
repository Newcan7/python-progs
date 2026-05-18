s1=input("enter first word")
s2=input("enter second word")
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("no anagram")
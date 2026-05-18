l=["  iphone-14 Pro   ",
"  SAMSUNG   galaxy  S23",
"oneplus_  11",
"  Pixel--7   Pro",
" xiaomi 13  "
]
for i in range(len(l)):
    l[i]=l[i].replace("_"," ")
    l[i]=l[i].replace("-"," ")
    l[i] = " ".join(l[i].split())
    l[i]=l[i].title()
print(l)
l=[{"name":"abu","marks":94,"age":20},
   {"name":"anirudh","marks":99,"age":19},
   {"name":"ribhav","marks":91,"age":20},
   {"name":"abhinav","marks":95,"age":21},
    {"name":"test","marks":60,"age":61}]
t= filter(lambda x : x["marks"] >90 ,l)
l1=list(t)
sortedl= sorted(l1,key=lambda x : x["marks"])
print(sortedl)
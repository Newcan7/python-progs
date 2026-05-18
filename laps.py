l=[{"name":"Abu","lap1":9,"lap2": 9,"lap3": 9},{"name":"oini","lap1":11,"lap2": 9,"lap3": 9},{"name":"test","lap1":9,"lap2": 6,"lap3": 9}]
def check_laps(a):
    return (a["lap1"]<10 and a["lap3"]<10 and a["lap3"]<10)
final=list(filter(check_laps,l))
print(final)
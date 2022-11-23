l=[("A",1),("B",2),("C",3),("D",4)]
d={}

for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)

d={1:"ram",2:"shyam",3:"karan"}

print(d)
print()
d1=d.copy()
print(d1)

print()
d2={4:"Laxman",5:"harish"}

print()
print(d2)
print("merge two dictionary".center(80,"*"))
print()
d.update(d2)
print(d)

intTuple = ()
numb = int(input("Please enter the Total Tuple Items to store = "))
for i in range(1, numb + 1):
    value = int(input("Please enter %d Tuple Item = " %i))
    intTuple += (value,)

print("Tuple Items = ", intTuple)

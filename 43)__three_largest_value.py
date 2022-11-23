from heapq import nlargest
mydict={"A":5431,"B":4320,"C":1100,"D":5432,"E":2209}
threelargest=nlargest(3 , mydict, key=mydict.get)
print(threelargest)


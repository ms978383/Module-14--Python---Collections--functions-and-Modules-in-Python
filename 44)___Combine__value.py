from collections import Counter

itemlist=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]

result=Counter()

for d in itemlist:
    result[d["item"]] +=d["amount"]
print(result)    

"""
ZIP() METHOD :


Python zip() method takes iterable or containers and returns
a single iterator object, having mapped values from all the
containers.
It is used to map the similar index of multiple containers so
that they can be used just using a single entity.

"""

key=[1,2,3]
value=["Orange","Mango","Banana"]
print("keys are :",key)
print("values are :",value)

fruit_dict=dict(zip(key,value))

print("map(zip) in dict.:",fruit_dict)



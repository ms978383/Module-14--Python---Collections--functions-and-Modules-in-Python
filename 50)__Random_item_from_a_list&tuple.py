"""
 RANDOM ITEM FROM A LIST AND TUPLE:

In Python, you can randomly sample elements from a list with choice(),
sample(), and choices() of the random module.
These functions can also be applied to a string and tuple.
choice() returns one random element, and sample() and choices()
return a list of multiple random elements.


e.g:
    -   Pick a random element                   :   random.choice()
    -  Random sample without replacement        :   random.sample()
    -  Random sample with replacement           :   random.choices()
    -  Initialize the random number generator   :   random.seed()

"""

import random

l = [0, 1, 2, 3, 4]

print(random.choice(l))

print(random.choice(("mks","tops","career")))


print(random.choice("python"))

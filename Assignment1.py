# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:23:18 2019

@author: Vamshi Krishna
"""

population={"shangai":17.8,"istanbul":13.3,"karachi":13.0,"mumbai":12.5}
print(population)

animals={'dog':[20,10,15,8,32,15],'cat':[3,4,2,8,2,4],'rabbits':[2,3,3],'fish':[0,3,0.5,0.8,0.3,1]}
print(animals['dog'])
print(animals['dog'] [3])
print(animals['rabbits'])
print(animals['fish'])


a=[1,2,2,3,3,3,4,4,4,4]
b=set(a)
print(b)
print(len(a))
print(len(b))
print(len(a)-len(b))


tuple_a=3,4
tuple_b=(3,4)
print(tuple_a)
print(tuple_b)
print(tuple_a==tuple_b)
print(tuple_a[1])


names=["carol","albert","ben","donna"]
print("&".join(names))

import numpy as np
vamshi= np.array([45,62,54,23,32,87,90])
print()
print('vamshi = ',vamshi)
print()


import pandas as pd 
import numpy as np 

s1 = pd.Series([1,2,3,4,5,6] , ['a','b','c','d','e','f'])
print(s1)
print(type(s1))

arr = np.array([10,20,30,40,50])
s2 = pd.Series(arr)
print(s2)

s = pd.Series([100, 200, 300], index=['First', 'Second', 'Third'], name='Revenue')
print(f"values : {s.values}")
print(f"type : {type(s.values)}")
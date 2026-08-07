import pandas as pd 
import numpy as np 

s1 = pd.Series([1,2,3,4,5,6] , ['a','b','c','d','e','f'])
print(s1)
print(type(s1))

arr = np.array([10,20,30,40,50])
s2 = pd.Series(arr)
print(s2)

print("""
 ---------------------------------------------------------------------------- 
                          series properties                              
 ---------------------------------------------------------------------------- 
""")
s3 = pd.Series([100, 200, 300], index=['First', 'Second', 'Third'], name='Revenue')
print(f"Series : {s3}")

print(f"values : {s3.values}")
print(f"type : {type(s3.values)}")
print(f"dtype : {s3.dtype}")
print(f"shape : {s3.shape}")


print("""
# ---------------------------------------------------------------------------- #
#                           accesing series elements                           #
# ---------------------------------------------------------------------------- #
""")
s4 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(f"Series:\n{s4}")



import numpy as np 

myarr = np.array([[3,4,6,7]] ,np.int8 )

print(myarr)
print(myarr[0,1])
print(myarr.shape)
print(myarr.dtype)
myarr[0,1] = 9
print(myarr[0,1])

#convertion from other python structure : 
listarray = np.array([[1,2,3], [4,5,6], [8,9,0]])
print(listarray.dtype)
print(listarray.shape)

#for zero array list
print(np.zeros((1,5)))

#use of arange function for creating array in numpy (arange function)
print(np.arange(5)) 

#some important function 

# 1.reshape
arr = np.arange(50)

print(arr.reshape(2,25)) # make sure all element get place to use reshape function
print(arr.ravel()) # to convert this arry into 1d array


# ---------------------------------------------------------------------------- #
#                                  Numpy axis                                  #
# ---------------------------------------------------------------------------- #


x = [[1,2,3], [4,5,6], [7,8,9]]

myar = np.array(x)
print(myar)

print(myar.sum(axis=0))
print(myar.sum(axis=1))
print(myar.T)  # convert array to its transpose 

myar.flat    # (attribute) make itret that i can use into loops to process on each vlaues one by one 
for item in myar.flat: 
    print(item)


one = np.array([1,2,3,4,5])
print(one.argmax()) # (method which use : ())
#argmax() : give max value index 
#argmin() : give min value index
#argshort() : give array index in that way which we can use to sort array


# ---------------------------------------------------------------------------- #
#                            mathematical operations                           #
# ---------------------------------------------------------------------------- #
myar2 = np.array([[1,3,5], [5,7,8], [3,4,6]])
print(myar + myar2)
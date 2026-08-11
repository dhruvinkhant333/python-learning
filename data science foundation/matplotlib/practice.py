import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
x = np.arange(10)
y = x + 1
plt.plot(x, y)
plt.show()

x = np.arange(10)
y1 = 1 - x
plt.plot(x, y, x, y1)
plt.show()

n = 3 
t = np.arange(0, np.pi*2, 0.05)
y = np.sin( n * t)
plt.plot(t , y)
plt.show()

n = 5 
x = np.arange(n)
y = np.random.rand(n)
plt.bar(x, y)
plt.show()


fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_title('bar graph')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

x = np.arange(10)

plt.subplot (2, 2, 1)
plt.plot(x, x)
plt.title("linear")

plt.subplot(2, 2, 2)
plt.plot(x, x*x)
plt.title("quadratic")

plt.subplot(2, 2, 3)
plt.plot(x, np.sqrt(x))
plt.title("square root")

plt.subplot(2, 2, 4)
plt.plot(x, np.log(x))
plt.title('Log')
plt.tight_layout()
plt.show()


fig, ax = plt.subplots(2, 2)
ax[0][0].plot(x, x)
ax[0][0].set_title('Linear')
ax[0][1].plot(x, x*x)
ax[0][1].set_title('Quadratic')
ax[1][0].plot(x, np.sqrt(x))
ax[1][0].set_title('Square Root')
ax[1][1].plot(x, np.log(x))
ax[1][1].set_title('Log')
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,top=0.9,
                    wspace=0.4,
                    hspace=0.4)
plt.show()


# ---------------------------------------------------------------------------- #
#                                    pandas                                    #
# ---------------------------------------------------------------------------- #
# reate a simple series using list as follows:
s1 = pd.Series([1, 2, 3, 4, 5])
print(type(s1))
print(s1)


# We can also create a series with the following code:
s2 = pd.Series(np.arange(5), dtype= np.uint8)
print(s2)

# We can create a series by using an already deined Ndarray as
# follows
arr1 = np.arange(5 , dtype = np.uint8)
s3 = pd.Series(arr1 , dtype = np.int16)
print(s3)
s3

# We can check the values of the members of the series as follows:
print(s3.values)

# We can also check the values of the series with the following code:
print(s3.array)

# We can check the index of the series:
print(s3.index)

# We can check the datatype as follows:
print(s3.dtype)

# We can check the shape as follows:
print(s3.shape)

# We can check the size as follows:
print(s3.size)

# We can check the number of bytes as follows:
print(s3.nbytes)

# And we can check the dimensions as follows:
print(s3.ndim)


# ----------------------------- Pandas Dataframes ---------------------------- #


# create a dataframe. Let’s create a dictionary of population data for cities as follows:
data = {'city': ['Bangalore', 'Bangalore',
'Bangalore','Mumbai', 'Mumbai', 'Mumbai'],
'year': [2020, 2021, 2022, 2020, 2021,2022,],
'population': [10.0, 10.1, 10.2, 5.2, 5.3,5.5]
}

# we can creat a dataframe using this dictionary : 

df1 = pd.DataFrame(data)
print(df1)

# we can see the first five records of the dataframe with use of this code :
print(df1.head())

# we can create dataframe with specific order of columns as follows : 
df2 = pd.DataFrame(data, columns=['year', 'city', 'population'])
print(df2)

# -------------------- visualizing the data in Dataframes -------------------- #

df1 = pd.DataFrame()
df1 ['A'] = pd.Series(list(range(100)))
df1 ['B'] = np.random.randn(100, 1)
print(df1)

df1.plot(x='A', y='B')
plt.show()

# other plotting methods. We will create a
# dataset of four columns.

df2 = pd.DataFrame(np.random.rand(10,40) , columns=['A', 'B', 'C', 'D'] )
print(df2)

# Let us plot bar graphs as follows:
df2.plot.bar()
plt.show()

# We can plot these graphs horizontally too as follows:
df2.plot.barh()
plt.show()


# We can stack upper bar graph as follows:
df2.plot.bar(stacked = True)
plt.show()

# We can have horizontal stacked bars as follows:
df2.plot.barh(stacked = True)
plt.show()
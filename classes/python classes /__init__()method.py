# Create a class named Person, use the __init__() method to assign values for name and age:

class person : 
    def __init__(self, name , age) : 
        self.name = name
        self.age = age 

p1 = person("jay" , 19)

print (p1.name)
print (p1.age)



# Why Use __init__()?

#  without __init__ set properties manually for each object
class person : 
    pass 

p1 = person()
p1.name = "jay"
p1.age =20 

print(p1.name)
print(p1.age)

# Using __init__() makes it easier to create objects with initial values:
# as above first example 



# Default Values in __init__()
class person : 
    def __init__(self , name ,age = 19 ): 
        self.name = name 
        self.age = age 

p1 = person("mike")
p2 = person("joy" , 23 )

print (p1.name , p1.age )
print (p2.name , p2.age )

# The __init__() method can have as many parameters as you need
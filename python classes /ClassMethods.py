# ------------------------------- Class Methods ------------------------------ #
# Methods are functions that belong to a class. They define the behavior of objects created from the class.

# Example
# Create a method in a class:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

# Note: All methods must have self as the first parameter.





# -------------------------- Methods with Parameters ------------------------- #
# Methods can accept parameters just like regular functions:

# Example
# Create a method with parameters:

class calculater : 
  def add(self , a , b): 
    return a + b 
  def multiply(self , a , b): 
    return a*b
  
calc  = calculater()
 
print(calc.add(1,3))
print(calc.multiply(2,4))





# ----------------------- Methods Accessing Properties ----------------------- #
# Methods can access and modify object properties using self:

# Example
# A method that accesses object properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())



# ----------------------- Methods Modifying Properties ----------------------- #
# Methods can modify the properties of an object:

# Example
# A method that changes a property value

class Person: 
    def __init__(self, name , age): 
        self.name = name 
        self.age = age 

    def celebrate_birthday(self):
        self.age += 1
        print(f"happy birthday ! you are now {self.age} year old.")

p1 = Person("linus" , 21)
p1.celebrate_birthday()
p1.celebrate_birthday()


# --------------------------- The __str__() Method --------------------------- #
# The __str__() method is a special method that controls what is returned when the object is printed:

# Example
# Without the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

# Example
# With the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)




# ----------------------------- Multiple Methods ----------------------------- #
# A class can have multiple methods that work together:

# Example
# Create multiple methods in a class:
class playlist:

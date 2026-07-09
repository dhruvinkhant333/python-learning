# ----------------------------- Class Properties ----------------------------- #
# Properties are variables that belong to a class. They store data for each object created from the class.


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


# ----------------------------- Access Properties ---------------------------- #
# You can access object properties using dot notation:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)


# ----------------------------- Modify Properties ---------------------------- #
# You can modify the value of properties on objects:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)

# ----------------------------- Delete Properties ---------------------------- #
# You can delete properties from objects using the del keyword:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error


# ------------------- Class Properties vs Object Properties ------------------ #
# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

# Example
# Class property vs instance property:

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


# ------------------------ Modifying Class Properties ------------------------ #
# When you modify a class property, it affects all objects:

# Example
# Change a class property:

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

# ---------------------------- Add New Properties ---------------------------- #
# You can add new properties to existing objects:

# Example
# Add a new property to an object:

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)


# ------------------------------ CODE CHALLANGE ------------------------------ #
# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

class Student: 
    def __init__(self, name , grade): 
        self.name = name 
        self.grade = grade 

s1 = Student("anna" , "A")
print(s1.grade)

s1.grade = "B"
print(s1.grade)
    

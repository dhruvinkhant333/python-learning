# --------------------------- Python Encapsulation --------------------------- #

# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.



# ---------------------------- Private Properties ---------------------------- #
# In Python, you can make properties private by using a double underscore __ prefix:
class person : 
    def __init__(self , name , age): 
        self.name = name 
        self.__age = age #private property 
    
p1 = person("mike" , 23)
print(p1.name)
print(p1.__age) #this will cause an error


# GET PRIVATE PROPERTY VALUE : 

# to access a private property , you can creat a getter method : 
class person : 
    def __init__(self , name , age): 
        self.name = name 
        self.__age = age #private property 

    def get_age(self):
        return self.__age
    
p1 = person("mike" , 23)
print(p1.name)
print(p1.get_age())



# ------------------------ Set Private Property Value ------------------------ #

# To modify a private property, you can create a setter method.
# The setter method can also validate the value before setting it:


class person : 
    def __init__(self , name , age): 
        self.name = name 
        self.__age = age #private property 

    def get_age(self):
        return self.__age
    
    def set_age(self , age):
        if age > 0:
            self.__age = age 
        else: 
            print("age must be positive")

p1 = person("mike" , 23)
print(p1.get_age())

p1.set_age(45)
print(p1.get_age())



# -------------------------- Why Use Encapsulation? -------------------------- #

# Encapsulation provides several benefits:

# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified

class student: 
    def __init__(self , name):
        self.name = name
        self.__grade = 0 

    def set_grade(self , grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "passed"
        else:
            return "failed"
        
student = student("gwen")
student.set_grade(99)
print(student.name)
print(student.get_grade())
print(student.get_status())


# --------------------------- Protected Properties --------------------------- #

# Python also has a convention for protected properties using a single underscore _ prefix:
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't



# ----------------------------- Private Methods ------------------------------ #

# You can also make methods private using the double underscore prefix:

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    # Private method - cannot be called directly from outside the class
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error - private method cannot be accessed directly


# Note: Just like private properties with double underscores, private methods cannot be called 
# directly from outside the class. The __validate method can only be used by other methods inside the class.



# ------------------------------ Name Mangling ------------------------------- #

# Name mangling is how Python implements private properties and methods.
# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.
# For example, __age becomes _Person__age.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # This becomes _Person__age internally

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age)  # Prints: 30 (Not recommended!)

# Note: While you *can* access private properties using the mangled name, it's not recommended. 
# It defeats the purpose of encapsulation and makes your code harder to maintain.


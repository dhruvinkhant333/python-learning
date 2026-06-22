# # ---------------------------- Python Inheritance ---------------------------- #

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# --------------------------- Create a Parent Class -------------------------- #

# Any class can be a parent class, so the syntax is the same as creating any other class:

# Example
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person: 
    def __init__(self , fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"{self.firstname} , {self.lastname}")

p1 = Person("mike" , "tyson")
p1.printname()




# --------------------------- Create a Child Class --------------------------- #
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Student(Person):
  pass



# ------------------------ Add the __init__() Function ----------------------- #

# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# PARENT CLASS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printinfo(self):
        print(f"{self.name}, {self.age}")

# CHILD CLASS
class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(name, age)  # ✅ Get parent's properties
        self.grade = grade            # ✅ Add child's properties

# Using it
s1 = Student("Ali", 20, "A+")
s1.printinfo()           # ✅ Ali, 20
print(s1.grade)          # ✅ A+



# ------------------------- Use the super() Function ------------------------- #
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# PARENT CLASS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printinfo(self):
        print(f"{self.name}, {self.age}")

# CHILD CLASS
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # ✅ Get parent's properties
        self.grade = grade            # ✅ Add child's properties

# Using it
s1 = Student("Ali", 20, "A+")
s1.printinfo()           # ✅ Ali, 20
print(s1.grade)          # ✅ A+




# -------------------------------- Add Methods ------------------------------- #

# Example
# Add a method called welcome to the Student class:

# PARENT CLASS
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

# CHILD CLASS
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):  # ✅ NEW METHOD ONLY IN CHILD
        print(f"Welcome {self.firstname} {self.lastname} to class of {self.graduationyear}")

# Using it
s1 = Student("Ali", "Khan", 2025)
s1.printname()  # ✅ From parent: Ali Khan
s1.welcome()    # ✅ From child: Welcome Ali Khan to class of 2025


# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
class Person:
    def greet(self):
        print("Hello, I'm a person")

class Student(Person):
    def greet(self):  # ❌ SAME NAME as parent!
        print("Hello, I'm a student")

s1 = Student()
s1.greet()  # ❌ Hello, I'm a student (CHILD'S VERSION USED!)
            # Parent's greet() is IGNORED!

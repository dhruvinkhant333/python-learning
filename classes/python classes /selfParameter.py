 # ---------------------------- The self Parameter ---------------------------- #

# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.

class student : 
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 

    def greet(self):
        print (f"hi {self.name} , your age is {self.age}")

p1 = student("mike" , 19)
p1.greet()

# Note: The self parameter must be the first parameter of any method in the class.


# ------------------------------- Why Use self? ------------------------------ #

# Without self, Python would not know which object's properties you want to access




# ------------------- self Does Not Have to Be Named "self" ------------------ #
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

# ------------------------- Calling Methods with self ------------------------ #
class Person: 
    def __init__(self, name): 
        self.name = name 

    def greet(self): 
        return f"Hello , {self.name}"
      
    def welcome(self): 
        massage = self.greet()
        print(f"{massage} ! welcome to our website.")

p1 = Person("joy")
p1.welcome()



# ----------------------------- CODE CHALLENGE 1 ----------------------------- #

# Create a class called Car
# Add an __init__ method with a brand parameter, and store it as a property
# Add a method called show that prints the brand
# Create an object c1 of the Car class with brand "Ford"
# Call the show method on c1

class car : 
    def __init__(self , brand ): 
        self.brand = brand 

    def show(self):
        print (f"{self.brand}")
    
c1 = car("Ford")
c1.show()
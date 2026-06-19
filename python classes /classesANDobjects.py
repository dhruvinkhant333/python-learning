sel#Create a class named MyClass, with a property named x:
class myclass:
    x = 5
#Create an object named p1, and print the value of x:

p1 = myclass()
print(p1.x)

#delete the p1 object 
del p1 


#Create three objects from the MyClass class:

p1 = myclass()
p2 = myclass()
p3 = myclass()

print(p1.x)
print(p2.x)
print(p3.x)


#The pass Statement
#class definitions cannot be empty, 
#but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class person: 
    pass 


#EXAMPLE : 1 

# Create a class called Person
# Add an __init__ method that takes name and age as parameters
# Add a method called greet that prints "Hello, my name is " followed by the name
# Create an object p1 of the class with name "John" and age 36
# Call the greet method on p1
 
class person:

    def __init__(self , name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = person("john", 36)

p1.greet()
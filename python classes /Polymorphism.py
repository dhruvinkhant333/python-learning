# ---------------------------- Python Polymorphism --------------------------- #

# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# ---------------------------- Class Polymorphism ---------------------------- #

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()

# Example 1: Basic Polymorphism
class Car:
  def __init__(self, brand):
    self.brand = brand

  def move(self):
    print(f"{self.brand} car is driving on the road 🚗")


class Boat:
  def __init__(self, brand):
    self.brand = brand

  def move(self):
    print(f"{self.brand} boat is sailing on the water 🚤")


class Plane:
  def __init__(self, brand):
    self.brand = brand

  def move(self):
    print(f"{self.brand} plane is flying in the sky ✈️")


# Create objects and call move() method
car1 = Car("Toyota")
boat1 = Boat("Yamaha")
plane1 = Plane("Boeing")

car1.move()
boat1.move()
plane1.move()




# Example 2: Polymorphism with Loop and List
# The same method name, but different behavior based on the object type

vehicles = [car1, boat1, plane1]

print("\n--- Calling move() on all vehicles ---")
for vehicle in vehicles:
  vehicle.move()




# Example 3: Function using Polymorphism
# A function that accepts any object with a move() method

def travel(vehicle):
  """This function works with any object that has a move() method"""
  print("Starting journey...")
  vehicle.move()
  print("Journey complete!\n")


print("--- Using Polymorphic Function ---")
travel(car1)
travel(boat1)
travel(plane1)




# Example 4: Inheritance with Polymorphism
# Parent class with a method, child classes override it

class Animal:
  def speak(self):
    print("Some animal sound...")


class Dog(Animal):
  def speak(self):
    print("Dog barks: Woof! Woof! 🐕")


class Cat(Animal):
  def speak(self):
    print("Cat meows: Meow! Meow! 🐱")


class Cow(Animal):
  def speak(self):
    print("Cow moos: Moo! Moo! 🐄")


# Demonstrate polymorphism with animals
animals = [Dog(), Cat(), Cow()]

print("\n--- Animal Sounds (Polymorphism with Inheritance) ---")
for animal in animals:
  animal.speak()




# Key Takeaways:
# 1. Different classes can have methods with the same name
# 2. Each class implements the method in its own way
# 3. The same function can work with different object types
# 4. This makes code more flexible and reusable
# 5. Polymorphism is the foundation of flexible object-oriented design


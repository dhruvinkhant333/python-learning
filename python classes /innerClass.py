# --------------------------- Python Inner Classes --------------------------- #

# An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.

# Inner classes are useful for grouping classes that are only used in one place, making your code more organized.
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)


# ------------------ Accessing Inner Class from the Outside ------------------ #

# To access the inner class, create an object of the outer class, and then create an object of the inner class:

class outer:
    def __init__(self , name):
        self.name = "outer"
    class inner:
        def __init__(self , name):
            self.name = "inner"

        def display(self):
           print("hello from inner class")
          
outer = outer()
inner = outer.inner()
inner.display()


# ------------------ Accessing Outer Class from Inner Class ------------------ #

# Inner classes in Python do not automatically have access to the outer class instance.

# If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:

class outer:
    def __init__(self):
      self.name = "mile"

    class Inner:
        def __init__(self, outer):
           self.outer = outer 

        def display(self):
           print(f"outer class name : {self.outer.name}")

outer = outer()
inner = outer.inner(outer)
inner.display()


# ----------------------- Real-World Example: Car with Engine ----------------------- #

# This is a practical example showing how inner classes are useful in real applications.
# A Car has an Engine, so Engine is an inner class of Car.

class Car:
  def __init__(self, brand, model):
    # Outer class properties - the car's details
    self.brand = brand
    self.model = model
    # Create an Engine object automatically when a Car is created
    # This is useful: every car should have an engine
    self.engine = self.Engine()

  # Inner class - Engine is only used by Car, so it's nested inside
  class Engine:
    def __init__(self):
      # Engine has its own properties
      self.status = "Off"

    def start(self):
      # Method to start the engine
      self.status = "Running"
      print("Engine started")

    def stop(self):
      # Method to stop the engine
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    # Car's method that uses the Engine's status
    # This shows how outer class methods can access inner class properties
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")


# --- How it works: Step by step --- #

# Step 1: Create a Car object
car = Car("Toyota", "Corolla")
# This automatically creates:
#   - car.brand = "Toyota"
#   - car.model = "Corolla"
#   - car.engine = Engine object with status "Off"

# Step 2: Try to drive without starting engine
car.drive()
# Output: "Start the engine first!"
# Reason: car.engine.status is "Off"

# Step 3: Start the engine
car.engine.start()
# Output: "Engine started"
# Now: car.engine.status = "Running"

# Step 4: Now we can drive
car.drive()
# Output: "Driving the Toyota Corolla"
# Reason: car.engine.status is "Running"

# Step 5: Stop the engine
car.engine.stop()
# Output: "Engine stopped"
# Now: car.engine.status = "Off"




# ---------------------- Create multiple inner classes: ---------------------- #

# A class can have MULTIPLE inner classes.
# This is useful when the outer class is composed of multiple related components.
# Example: A Computer has both CPU and RAM, so both are inner classes.

class Computer:
  def __init__(self):
    # When a Computer is created, it automatically creates instances of CPU and RAM
    # This is the power of inner classes - they're tightly bound to the outer class
    self.cpu = self.CPU()      # Create CPU inner class object
    self.ram = self.RAM()      # Create RAM inner class object

  # First inner class - CPU handles processing
  class CPU:
    def process(self):
      # CPU's responsibility: process data
      print("Processing data...")

  # Second inner class - RAM handles storing data
  class RAM:
    def store(self):
      # RAM's responsibility: store data
      print("Storing data...")

# --- Step-by-step execution --- #

# Step 1: Create a Computer object
computer = Computer()
# This automatically creates:
#   - computer.cpu = CPU object
#   - computer.ram = RAM object

# Step 2: Use the CPU
computer.cpu.process()
# Output: "Processing data..."

# Step 3: Use the RAM
computer.ram.store()
# Output: "Storing data..."


# --- Why use multiple inner classes? --- #
# 1. Organization: CPU and RAM are grouped together under Computer
# 2. Encapsulation: These classes are only used by Computer
# 3. Modularity: Each component has its own responsibility
# 4. Clarity: Anyone reading the code knows CPU and RAM belong to Computer
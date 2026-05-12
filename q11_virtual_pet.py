"""
Question 1: The Virtual Pet

Write a Python program that uses a closure to manage the state of a virtual pet.

Requirements:
- Outer Function (adopt_pet): Takes pet_name, initializes energy (50) and happiness (50), returns inner function
- Inner Function (interact): Takes action ("feed", "play", or "status")
  - "feed": Increases energy by 20. Returns "[pet_name] was fed! Energy is now [energy]."
  - "play": Decreases energy by 15, increases happiness by 20. 
    If energy < 15, return "[pet_name] is too tired to play!" without changing stats.
  - "status": Returns a string with pet's name, current energy, and current happiness
- Must use nonlocal to modify energy and happiness
"""


def adopt_pet(pet_name):
    """
    Creates a virtual pet with state management using closure.
    
    Args:
        pet_name (str): Name of the pet
    
    Returns:
        function: The interact function that manages pet interactions
    """
    energy = 50
    happiness = 50
    
    def interact(action):
        """
        Manages pet interactions and state changes.
        
        Args:
            action (str): The action to perform ("feed", "play", or "status")
        
        Returns:
            str: Message describing the result of the action
        """
        nonlocal energy, happiness
        
        if action == "feed":
            energy += 20
            return f"{pet_name} was fed! Energy is now {energy}."
        
        elif action == "play":
            if energy < 15:
                return f"{pet_name} is too tired to play!"
            energy -= 15
            happiness += 20
            return f"{pet_name} played! Happiness: {happiness}, Energy: {energy}."
        
        elif action == "status":
            return f"{pet_name} - Energy: {energy}, Happiness: {happiness}"
        
        else:
            return "Unknown action. Try 'feed', 'play', or 'status'."
    
    return interact


# Expected Output Examples:
if __name__ == "__main__":
    # Create a virtual pet named "Fluffy"
    fluffy = adopt_pet("Fluffy")
    
    print(fluffy("status"))        # Fluffy - Energy: 50, Happiness: 50
    print(fluffy("feed"))          # Fluffy was fed! Energy is now 70.
    print(fluffy("play"))          # Fluffy played! Happiness: 70, Energy: 55.
    print(fluffy("play"))          # Fluffy played! Happiness: 90, Energy: 40.
    print(fluffy("play"))          # Fluffy played! Happiness: 110, Energy: 25.
    print(fluffy("play"))          # Fluffy played! Happiness: 130, Energy: 10.
    print(fluffy("play"))          # Fluffy is too tired to play!
    print(fluffy("feed"))          # Fluffy was fed! Energy is now 30.
    print(fluffy("status"))        # Fluffy - Energy: 30, Happiness: 130

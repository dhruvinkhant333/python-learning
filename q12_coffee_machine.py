"""
Question 2: The Coffee Machine

Create a closure that simulates a coffee machine tracking its resources.

Requirements:
- Outer Function (setup_coffee_machine): Takes no arguments, initializes water (500 ml) and beans (100 grams)
- Inner Function (brew): Takes drink_type ("espresso", "americano", or "refill")
  - "espresso": requires 50ml water and 18g beans
  - "americano": requires 150ml water and 18g beans
  - If resources available: deduct and return "Enjoy your [drink_type]!"
  - If not enough: return "Not enough resources."
  - "refill": resets water to 500 and beans to 100, return "Machine refilled!"
"""


def setup_coffee_machine():
    """
    Sets up a coffee machine with resource tracking using closure.
    
    Returns:
        function: The brew function that manages coffee making
    """
    water = 500  # ml
    beans = 100  # grams
    
    def brew(drink_type):
        """
        Brews a coffee drink or refills the machine.
        
        Args:
            drink_type (str): Type of drink ("espresso", "americano", or "refill")
        
        Returns:
            str: Message describing the result of the action
        """
        nonlocal water, beans
        
        if drink_type == "espresso":
            if water >= 50 and beans >= 18:
                water -= 50
                beans -= 18
                return "Enjoy your espresso!"
            else:
                return "Not enough resources."
        
        elif drink_type == "americano":
            if water >= 150 and beans >= 18:
                water -= 150
                beans -= 18
                return "Enjoy your americano!"
            else:
                return "Not enough resources."
        
        elif drink_type == "refill":
            water = 500
            beans = 100
            return "Machine refilled!"
        
        else:
            return "Unknown drink type. Try 'espresso', 'americano', or 'refill'."
    
    return brew


# Expected Output Examples:
if __name__ == "__main__":
    machine = setup_coffee_machine()
    
    print(machine("espresso"))      # Enjoy your espresso!
    print(machine("espresso"))      # Enjoy your espresso!
    print(machine("americano"))     # Enjoy your americano!
    print(machine("espresso"))      # Enjoy your espresso!
    print(machine("espresso"))      # Enjoy your espresso!
    print(machine("espresso"))      # Enjoy your espresso!
    print(machine("espresso"))      # Not enough resources.
    print(machine("refill"))        # Machine refilled!
    print(machine("americano"))     # Enjoy your americano!

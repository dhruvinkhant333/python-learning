"""
QUESTION 3: Event Handler with Loop (Tricky!)
Solution for the closure late binding bug
"""

# ============================================================================
# BROKEN VERSION - Shows the problem
# ============================================================================
def setup_buttons_broken():
    """
    Creates 3 buttons. When clicked, each should print its button number
    But this code has a closure bug!
    
    Problem: button_id is captured by reference, not by value.
    By the time any button's on_click() is called, button_id is 3 for all.
    """
    buttons = []
    for button_id in range(1, 4):
        def on_click():
            print(f"Button {button_id} clicked!")  # ← BUG HERE
        buttons.append(on_click)
    return buttons


# ============================================================================
# FIXED VERSION - Solution using default argument
# ============================================================================
def setup_buttons_fixed():
    """
    Fixed version: Use default argument to capture button_id by VALUE
    
    The key: id=button_id in the function signature captures the current
    value of button_id as a default argument, creating a new binding
    for each iteration.
    """
    buttons = []
    for button_id in range(1, 4):
        def on_click(id=button_id):  # ← SOLUTION: capture by value
            print(f"Button {id} clicked!")
        buttons.append(on_click)
    return buttons


# ============================================================================
# ALTERNATIVE FIX - Using a closure factory function
# ============================================================================
def setup_buttons_fixed_v2():
    """
    Alternative: Create a factory function that returns on_click
    This explicitly creates a new closure scope for each button
    """
    def create_button_handler(button_id):
        def on_click():
            print(f"Button {button_id} clicked!")
        return on_click
    
    buttons = []
    for button_id in range(1, 4):
        buttons.append(create_button_handler(button_id))
    return buttons


# ============================================================================
# TEST & DEMONSTRATE THE BUG AND FIX
# ============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("BROKEN VERSION - Shows the bug:")
    print("=" * 60)
    buttons_broken = setup_buttons_broken()
    buttons_broken[0]()  # Will print "Button 3 clicked!" (WRONG!)
    buttons_broken[1]()  # Will print "Button 3 clicked!" (WRONG!)
    buttons_broken[2]()  # Will print "Button 3 clicked!" (CORRECT but for wrong reason)
    
    print("\n" + "=" * 60)
    print("FIXED VERSION (Method 1 - Default Argument):")
    print("=" * 60)
    buttons_fixed = setup_buttons_fixed()
    buttons_fixed[0]()  # Should print "Button 1 clicked!"
    buttons_fixed[1]()  # Should print "Button 2 clicked!"
    buttons_fixed[2]()  # Should print "Button 3 clicked!"
    
    print("\n" + "=" * 60)
    print("FIXED VERSION (Method 2 - Factory Function):")
    print("=" * 60)
    buttons_fixed_v2 = setup_buttons_fixed_v2()
    buttons_fixed_v2[0]()  # Should print "Button 1 clicked!"
    buttons_fixed_v2[1]()  # Should print "Button 2 clicked!"
    buttons_fixed_v2[2]()  # Should print "Button 3 clicked!"
    
    print("\n" + "=" * 60)
    print("WHY THIS HAPPENS:")
    print("=" * 60)
    print("""
    The Bug (Late Binding):
    - When you create a closure inside a loop, it captures the VARIABLE,
      not the VALUE at that moment
    - All closures share the same reference to 'button_id'
    - After the loop ends, button_id = 3
    - So all closures print 3!
    
    The Fix (Method 1 - Default Argument):
    - Use id=button_id as a default parameter
    - Default arguments are evaluated at function DEFINITION time
    - Each iteration creates a new binding: id=1, id=2, id=3
    
    The Fix (Method 2 - Factory Function):
    - Create a factory function that returns the closure
    - The factory's parameter creates a new scope for each call
    - Each returned closure captures a different 'button_id' value
    """)

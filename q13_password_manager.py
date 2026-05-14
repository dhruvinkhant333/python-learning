"""
Question 3: Password Manager

Create a closure that generates passwords but tracks how many times a specific user 
has requested one, automatically incrementing a number at the end of the password.

Requirements:
- Outer Function (password_manager): Takes base_word, initializes version_counter to 1
- Inner Function (get_new_password): Takes no arguments
  - Returns a string combining base_word and current version_counter (e.g., "SecretWord1")
  - Then increments version_counter by 1 for the next call
"""


def password_manager(base_word):
    """
    Creates a password generator with automatic version tracking using closure.
    
    Args:
        base_word (str): The base word for the password
    
    Returns:
        function: The get_new_password function that generates versioned passwords
    """
    version_counter = 1
    
    def get_new_password():
        """
        Generates a new password by appending the current version number.
        
        Returns:
            str: Password in format "[base_word][version_counter]"
        """
        nonlocal version_counter
        password = f"{base_word}{version_counter}"
        version_counter += 1
        return password
    
    return get_new_password


# Expected Output Examples:
if __name__ == "__main__":
    # Create a password manager for a specific user
    alice_passwords = password_manager("SecurePass")
    bob_passwords = password_manager("MySecret")
    
    # Alice requesting passwords
    print(alice_passwords())  # SecurePass1
    print(alice_passwords())  # SecurePass2
    print(alice_passwords())  # SecurePass3
    
    # Bob requesting passwords (independent counter)
    print(bob_passwords())    # MySecret1
    print(bob_passwords())    # MySecret2
    
    # Alice continues from where she left off
    print(alice_passwords())  # SecurePass4
    print(bob_passwords())    # MySecret3
    print(bob_passwords())    # MySecret4

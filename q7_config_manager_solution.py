# ============================================================================
# QUESTION 7: Configuration Manager - SOLUTION
# ============================================================================
# Create a closure that manages application configuration

def create_config_manager():
    """
    Returns a dictionary with:
    - set_config(key, value) - sets a config value
    - get_config(key) - gets a config value
    - reset() - clears all config
    """
    config = {}
    
    def set_config(key, value):
        config[key] = value
    
    def get_config(key):
        return config.get(key)
    
    def reset():
        config.clear()
    
    return {
        'set_config': set_config,
        'get_config': get_config,
        'reset': reset
    }


# Test it
config = create_config_manager()
config['set_config']('theme', 'dark')
config['set_config']('language', 'en')
print(f"Theme: {config['get_config']('theme')}")  # Should be 'dark'
print(f"Language: {config['get_config']('language')}")  # Should be 'en'

# Test reset
config['reset']()
print(f"Theme after reset: {config['get_config']('theme')}")  # Should be None

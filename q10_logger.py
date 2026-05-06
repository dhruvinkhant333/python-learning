# ============================================================================
# QUESTION 10: Logger with Closure
# ============================================================================

def create_logger(log_prefix):
    """
    Returns a function that logs messages with a prefix
    """
    def logger(message):
        # The inner function has access to log_prefix from the outer scope
        print(f"{log_prefix} {message}")
    
    return logger

# Test it
if __name__ == "__main__":
    info_log = create_logger("[INFO]")
    error_log = create_logger("[ERROR]")
    
    info_log("Application started")  # Should print: [INFO] Application started
    error_log("File not found")      # Should print: [ERROR] File not found
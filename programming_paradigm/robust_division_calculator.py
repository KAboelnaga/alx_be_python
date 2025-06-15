def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling exceptions and returning a meaningful message.
    
    Args:
        numerator (str): The numerator as a string.
        denominator (str): The denominator as a string.
    
    Returns:
        str: The result of the division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / denom:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
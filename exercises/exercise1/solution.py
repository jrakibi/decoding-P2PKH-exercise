def sum_list(numbers):
    """
    Calculate the sum of all numbers in the list.
    
    Args:
        numbers: A list of numbers (integers or floats)
        
    Returns:
        The sum of all numbers in the list, or 0 if the list is empty
    """
    if not numbers:
        return 0
    return sum(numbers) 
import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    '''
     Returns a list of unique random numbers within a specified range.

     @param min: int - The minimum number in the range (inclusive).
     @param max: int - The maximum number in the range (inclusive).
     @param quantity: int - The number of unique random numbers to generate.
     
     @return: list - A list of unique random numbers.
    '''

    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except ValueError:
        raise ValueError("All parameters must be integers.")
        

    if quantity > (max - min + 1) or min < 1 or max > 1000:
        raise ValueError("Quantity exceeds the range of unique numbers available. min must be >= 1 and max must be <= 1000.")

    return random.sample(range(min, max + 1), quantity)

# Example usage:
numbers = get_numbers_ticket(1, 50, 10)
print(f"Generated numbers: {numbers}")
import re

def normalize_phone(num: str) -> str:
    '''
     Normalizes a phone number to the format +380XXXXXXXXX

     @param num: str - Phone number in various formats.

     @return: str - Normalized phone number in the format +380XXXXXXXXX.
    '''

    cleaned = re.sub(r'\D', '', num)
    
    if len(cleaned) == 10:
        return f"+380{cleaned}"
    elif len(cleaned) == 12 and cleaned.startswith("380"):
        return f"+{cleaned}"
    else:
        return None

# Example usage:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers:", sanitized_numbers)
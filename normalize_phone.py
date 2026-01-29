import re

def normalize_phone(num: str) -> str:
    '''
     Normalizes a phone number to the format +380XXXXXXXXX

     @param num: str - Phone number in various formats.

     @return: str - Normalized phone number in the format +380XXXXXXXXX.
    '''

    cleaned = re.sub(r'\D', '', num)
    
    if len(cleaned) == 9:
        return f"+380{cleaned}"
    if len(cleaned) == 10 and cleaned.startswith("0"):
        return f"+38{cleaned}"
    elif len(cleaned) == 12:
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
    "067\t123 4567",
    "(095) 123-4567\n",
    "+380 44 123 4567",
    "380501234567",
    "+38(050)123-45-67",
    "0501234567",
    "(050)1234567",
    "38050-123-45-67",
    "38050 123 45 67",
    "+432 10 123 45 67"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers:", sanitized_numbers)
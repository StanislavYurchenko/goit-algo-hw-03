from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''
     Returns the number of days from the given date to today.
     The date should be in the format 'YYYY-MM-DD'.

     @param date: str - The date to compare with today.
     
     @return: int - The number of days from the given date to today.
    '''
    
    try:
        normilized_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
    
        return (today - normilized_date).days

    except ValueError:
        raise ValueError("Date must be in 'YYYY-MM-DD' format")



# Example usage:
date_input = "2026-0101"
days_difference = get_days_from_today(date_input)
print(f"Days from {date_input} to today: {days_difference}")

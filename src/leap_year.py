
def check_leap_year(year:int) -> str:
    """
    Function to check if the given year is a leap year.
    
    Args:
    year: integer

    Returns:
    String "Leap Year" or "Not Leap Year"
    """
    if (year % 400 == 0) and (year % 100 == 0):
        return "Leap Year"
    elif (year % 4 == 0) and (year % 100 != 0):
        return "Leap Year"
    else:
        return "Not Leap Year"
    

print(check_leap_year(2000))

def check_leap_year(year:int) -> str:
    if (year % 400 == 0) and (year % 100 == 0):
        return "Leap Year"
    elif (year % 4 == 0) and (year % 100 != 0):
        return "Leap Year"
    else:
        return "Not Leap Year"
    

print(check_leap_year(2000))
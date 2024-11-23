# leap year or not

def leap_not(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
        
    else:
        return "not a leap year"
        

year = 1900
print(leap_not(year))
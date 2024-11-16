# Write a program to check if a given year is a leap year.  
"""
    Input: `year = 2020`  
   Output: `Leap Year`  
   Explanation: 2020 is divisible by 4 but not by 100, or it is divisible by 400, so it is a leap year.
"""

def checkLeapYear(year):
    if (year % 4 == 0): # if year is divisible by 4, then it is either century year or leap year
        if (year % 100 == 0):   # checking if it is a century year or not
            if (year % 400 == 0):    # century year is leap year only if it is divisible by 400
                return "Leap Year" 
            else:
                return "Not Leap Year"
        else:
            return "Leap Year"  # if any year is divisible by 4 and it is not a century year, then it is lep year
    else:
        return "Not Leap Year"  # if any year is not divisible by 4, then it is not a leap year
    
year = int(input("year = "))
result = checkLeapYear(year)
print(result)
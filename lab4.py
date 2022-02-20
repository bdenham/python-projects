################################################################################
#Developer Name:            Wyatt Denham
#program Name:              Denham_Chap4_PE12.py
#Due Date:                  01/28/2021
#Program Description:       This program takes in data from the user and
#                           informs the user of what season they were born in
#                           as well as if they were born on a leap year or not.

################################################################################
userName = ''
keepGoing = ''
MINIMUM_YEAR = 1900 # a very very old person!
MAXIMUM_YEAR = 2020 # a very very smart baby!
year = 0
season = ''
isLeapYear = 'was not'

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#Sentinal controlled while loop
while userName != 'zzz':
    # Get name input from user
    userName = input('\nEnter your name (zzz to stop): ')
    
    if userName == 'zzz':
        break
    
    # Get month input from user
    month = int(input('What month were you born? (1-12, January = 1): '))
    # Validate month 
    while month > 12 or month < 1:
        month = int(input('Your birth month must be between 1 (January) and 12 (December).\nWhat month were you born? '))
    
    if month == 12 or month == 1 or month == 2:
        season ='winter'
    elif month == 3 or month == 4 or month == 5:
        season = 'spring'
    elif month == 6 or month == 7 or month == 8:
        season = 'summer'
    else:
        season = 'fall' # because there's nothing else it could be.
    
    # Get year input from user  
    yearEntered = input('What year were you born? (Valid years are between 1900 and 2020): ')
    
    if isfloat(yearEntered):
        print("Year is invalid.")

    # Validate year 
    while year < MINIMUM_YEAR or year > MAXIMUM_YEAR:
        year = int(input('Your birth year must be between 1900 and 2020.\nWhat year were you born in? '))

    # Calculate leap year. Years
    if year % 4 == 0:
        if year % 400 == 0:
            isLeapYear = 'was'
    else:
        isLeapYear = 'was not'
        
    print(f'Hello {userName}! You were born in the {season} and {year} {isLeapYear} a leap year.')
  
print('\nEnd of program.')



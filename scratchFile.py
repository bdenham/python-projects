
#keep just in case
    #winter={1,2,12}
    #spring={3,4,5}
    #summer={6,7,8}
    #fall={9,10,11}

#         #month==(12 or 1 or 2) and (year/4==1):             #Winter not leap year
#     print('Hello ', name, ', you were born in winter not on a leap year.')
        
# while month==(12 or 1 or 2) and (year/4==0):           #Winter leap year
#     print('Hello ', name, ', you were born in winter on a leap year.')
        
# while month==(3 or 4 or 5) and (year/4==1):            #Spring not leap year
#     print('Hello ', name, ', you were born in spring not on a leap year.')
        
# while month==(3 or 4 or 5) and (year/4==0):            #Spring leap year 
#     print('Hello ', name, ', you were born in spring on a leap year.')
        
# while month==(6 or 7 or 8) and (year/4==1):            #Summer not leap year
#     print('Hello ', name, ', you were born in summer not on a leap year.')
            
# while month==(6 or 7 or 8) and (year/4==0):            #Summer leap year
#     print('Hello ', name, ', you were born in summer on a leap year.')

# while month==(9 or 10 or 11) and (year/4==1):          #Fall not leap year
#     print('Hello ', name, ', you were born in fall not on a leap year.')
        
# while month==(9 or 10 or 11) and (year/4==0):          #Fall leap year
#     print('Hello ', name, ', you were born in fall on a leap year.')

####################################################################################
# Developer Name:            Wyatt Denham
# Program Name:              Denham_Chap4_PE12.py
# Due Date:                  02/19/2022
# Program Description:       This program prompts a user for their name, birth 
#                            month, and birth year. It then greets the user by 
#                            name and tells them the season of the year they were
#                            born, as well as if their birth year was a leap year.

###################################################################################

# Constants
SENTINEL_VALUE = 'zzz'
USER_NAME_PROMPT = '\nEnter your name (or zzz to quit): '
BIRTH_MONTH_PROMPT = 'Enter your birth month number (between 1-12, 1 = Jan, 12 = Dec): '
BIRTH_YEAR_PROMPT = 'Enter your 4-digit birth year : '
INVALID_BIRTH_MONTH_MSG = 'Your birth month must be from 1-12: '
INVALID_BIRTH_YEAR_MSG = 'Your birth year must be a 4-digit year: '

# Variables
userName = ''
season = ''

# Helper functions
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isLeapYear(num):
    if num % 400 == 0:
        return 'was'
    elif num % 4 == 0:
        return 'was'
    else:
        return 'was not'


# Main program: Sentinel controlled while loop
while userName != SENTINEL_VALUE:
    # NAME input from user
    userName = input(USER_NAME_PROMPT)
    # Sentinel controlled exit
    if userName == SENTINEL_VALUE:
        break

    # MONTH input prompt and validation
    month = None
    while month is None:
        month_input = input(BIRTH_MONTH_PROMPT)
        try:
            month = int(month_input)
            while month > 12 or month < 1:
                try:
                    month = int(input(INVALID_BIRTH_MONTH_MSG))
                except:
                    print(f'{month} is not a number between 1-12.')
        except:
            print(f'{month_input} is not an integer.')

    # SEASON determined from month
    if month == 12 or month == 1 or month == 2:
        season = 'winter'
    elif month == 3 or month == 4 or month == 5:
        season = 'spring'
    elif month == 6 or month == 7 or month == 8:
        season = 'summer'
    else:
        season = 'fall'  # because there's nothing else it could be.

    # YEAR input prompt and validation
    year = None
    while year is None:
        year_input = input(BIRTH_YEAR_PROMPT)
        try:
            year = int(year_input)
        except:
            print(f'{year_input} is not an integer.')
        while year > 9999 or year < 1000:
            try:
                year = int(input(INVALID_BIRTH_YEAR_MSG))
            except:
                year = None
            
    # MAIN output
    print(f'Hello {userName}! You were born in the {season} of {year}, which {isLeapYear(year)} a leap year.')

print('\nProgram ended.\n')

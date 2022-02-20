
#keep just in case
    #winter={1,2,12}
    #spring={3,4,5}
    #summer={6,7,8}
    #fall={9,10,11}

   









        #month==(12 or 1 or 2) and (year/4==1):             #Winter not leap year
    print('Hello ', name, ', you were born in winter not on a leap year.')
        
while month==(12 or 1 or 2) and (year/4==0):           #Winter leap year
    print('Hello ', name, ', you were born in winter on a leap year.')
        
while month==(3 or 4 or 5) and (year/4==1):            #Spring not leap year
    print('Hello ', name, ', you were born in spring not on a leap year.')
        
while month==(3 or 4 or 5) and (year/4==0):            #Spring leap year 
    print('Hello ', name, ', you were born in spring on a leap year.')
        
while month==(6 or 7 or 8) and (year/4==1):            #Summer not leap year
    print('Hello ', name, ', you were born in summer not on a leap year.')
            
while month==(6 or 7 or 8) and (year/4==0):            #Summer leap year
    print('Hello ', name, ', you were born in summer on a leap year.')

while month==(9 or 10 or 11) and (year/4==1):          #Fall not leap year
    print('Hello ', name, ', you were born in fall not on a leap year.')
        
while month==(9 or 10 or 11) and (year/4==0):          #Fall leap year
    print('Hello ', name, ', you were born in fall on a leap year.')
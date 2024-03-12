# Leap Year
year = int(input('enter any year'))
if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(year,' was leap year') 
else:
    print(year, 'was not a leap year');
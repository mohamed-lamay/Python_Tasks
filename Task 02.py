def is_leap(year):
    #leap = False
    if (year % 4 == 0):

        if year % 100 == 0:
            print(False)
        if year % 400 == 0:
            print(True)
    else:
        print(False)
year = int(input("Enter a year: \n" ))
is_leap(year)




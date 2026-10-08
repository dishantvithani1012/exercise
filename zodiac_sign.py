'''
write a program to accept birth day and birth month from user as separate input. decide zodiac sign as sun rashi from below table 

    input : day 22 month = 4

    Aries: April 14 – May 14
    Taurus: May 15 – June 14
    Gemini: June 15 – July 16
    Cancer: July 17 – August 16
    Leo: August 17 – September 16
    Virgo: September 17 – October 16
    Libra: October 17 – November 15
    Scorpio: November 16 – December 15
    Sagittarius: December 16 – January 13
    Capricorn: January 14 – February 12
    Aquarius: February 13 – March 13
    Pisces: March 14 – April 13

    '''

day = int(input("Enter Day Of Birth : "))
month = int(input("Enter Month Of Birth : "))

# Days in each month 
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12 or day < 1 or day > days_in_month[month - 1]:
    print("Please Enter Valid Date Of Birth")

else:
    #Aries: April 14 - May 14
    if (month == 4 and day >= 14) or (month == 5 and day <= 14):
        print("Your Zodiac Sign Is Aries")

    #Taurus: May 15 - June 14
    elif (month == 5 and day >= 15) or (month == 6 and day <= 14):
         print("Your Zodiac Sign Is Taurus")

    #Gemini: June 15 - July 16
    elif (month == 6 and day >= 15) or (month == 7 and day <= 16):
        print("Your Zodiac Sign Is Gemini")

    #Cancer: July 17 - August 16
    elif (month == 7 and day >= 17) or (month == 8 and day <= 16):
         print("Your Zodiac Sign Is Cancer")

    #Leo: August 17 - September 16
    elif (month == 8 and day >= 17) or (month == 9 and day <= 16):
         print("Your Zodiac Sign Is Leo")

    #Virgo: September 17 - October 16
    elif (month == 9 and day >= 17) or (month == 10 and day <= 16):
         print("Your Zodiac Sign Is Virgo")

    #Libra: October 17 - November 15
    elif (month == 10 and day >= 17) or (month == 11 and day <= 15):
         print("Your Zodiac Sign Is Libra")

    #Scorpio: November 16 - December 15
    elif (month == 11 and day >= 16) or (month == 12 and day <= 15):
        print("Your Zodiac Sign Is Scorpio")

    #Sagittarius: December 16 - January 13
    elif (month == 12 and day >= 16) or (month == 1 and day <= 13):
         print("Your Zodiac Sign Is Sagittarius")

    #Capricorn: January 14 - February 12
    elif (month == 1 and day >= 14) or (month == 2 and day <= 12):
         print("Your Zodiac Sign Is Capricorn")

    #Aquarius: February 13 - March 13
    elif (month == 2 and day >= 13) or (month == 3 and day <= 13):
         print("Your Zodiac Sign Is Aquarius")

    #Pisces: March 14 - April 13
    else:
         print("Your Zodiac Sign Is Pisces")


print("Thank you")
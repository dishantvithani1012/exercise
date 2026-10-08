'''
write a program to accept birth day and birth month from user as separate input. decide zodiac sign as sun rashi from below table 

    input : day 22 month = 4

    Aries: March 21 – April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20

    '''

day = int(input("Enter Day Of Birth : "))
month =int(input(" Enter Month of Birth : "))

#Aries: March 21 – April 19
if (month == 3 and day >=22) or (month==4 and day <=19):
    print("Your Zodiac Sign Is Aries")

#Taurus: April 20–May 20
elif (month ==4 and day >=20 ) or (month==5 and day <=20):
    print("Your Zodiac Sign Is Taurus ")

#Gemini: May 21–June 21
elif (month ==5 and day >=21 ) or (month ==6 and day <=21):
    print("Your Zodiac Sign Is Gemini ")

#Cancer: June 22–July 22
elif (month == 6 and day >=22) or (month == 7 and day <= 22):
    print("Print Your Zodiac Sign IS Cancer ")

#Leo: July 23–August 22
elif (month ==  7 and day >= 23 ) or (month ==8 and day <=22):
    print("Your Zodiac Sign IS Leo")

# Virgo: August 23–September 22
elif (month == 8 and day >=23 ) or (month==9 and day <= 22):
    print("Your Zodiac Sing IS Vigro ")

#Libra: September 23–October 22
elif (month == 9 and day >=23 ) or (month== 10 and day<=22 ):
    print(" Your Zodiac Sign IS Libra ")

#Scorpio: October 24–November 21
elif (month == 10 and day >= 24 ) or (month ==11 and day <=21 ):
    print("Your Zodiac Sign Is Scorpio ")

#Sagittarius: November 22–December 21
elif (month == 11 and day >=22 ) or (month == 12 and day <=21 ):
    print(" Your Zodiac Sign Is Sagittarius ")

#Capricorn: December 22–January 19
elif (month == 12 and day >=22) or (month == 1 and day <=19):
    print(" Your Zodiac Sign Is Capricorn ")

#Aquarius: January 20–February 18
elif (month == 1 and day >= 20 ) or (month == 2 and day <=18 ):
    print("Your Zodiac Is Aquarius ")

#Pisces: February 19–March 20
elif (month == 2 and day >= 19 ) or (month == 3 and day <=20):
    print("Your Zodiac Sign Is Pisces ")

else :
    print("Please Enter Vailid Date Of Birth")

print("Thank you ")
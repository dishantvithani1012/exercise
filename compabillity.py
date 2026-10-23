'''
 write a program for male female marriage compatibility as per below link,  accept birth day and birth month from user as separate input. decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility

'''

male_day = int(input("Enter Day Of Birth(male) : "))
male_month = int(input("Enter Month Of Birth(male) : "))
print()


# Days in each month 
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if male_month < 1 or male_month > 12 or male_day < 1 or male_day > days_in_month[male_month - 1]:
    print("Please Enter Valid Date Of Birth")
    exit()

else:
    #Aries: April 14 - May 14
    if (male_month == 4 and male_day >= 14) or (male_month == 5 and male_day <= 14):
          Male_sign="Aries"

    #Taurus: May 15 - June 14
    elif (male_month == 5 and male_day >= 15) or (male_month == 6 and male_day <= 14):
          Male_sign="Taurus"

    #Gemini: June 15 - July 16
    elif (male_month == 6 and male_day >= 15) or (male_month == 7 and male_day <= 16):
          Male_sign="Gemini"

    #Cancer: July 17 - August 16
    elif (male_month == 7 and male_day >= 17) or (male_month == 8 and male_day <= 16):
          Male_sign="Cancer"

    #Leo: August 17 - September 16
    elif (male_month == 8 and male_day >= 17) or (male_month == 9 and male_day <= 16):
          Male_sign="Leo"

    #Virgo: September 17 - October 16
    elif (male_month == 9 and male_day >= 17) or (male_month == 10 and male_day <= 16):
          Male_sign="Virgo"

    #Libra: October 17 - November 15
    elif (male_month == 10 and male_day >= 17) or (male_month == 11 and male_day <= 15):
          Male_sign="Libra"

    #Scorpio: November 16 - December 15
    elif (male_month == 11 and male_day >= 16) or (male_month == 12 and male_day <= 15):
          Male_sign="Scorpio"

    #Sagittarius: December 16 - January 13
    elif (male_month == 12 and male_day >= 16) or (male_month == 1 and male_day <= 13):
          Male_sign="Sagittarius"

    #Capricorn: January 14 - February 12
    elif (male_month == 1 and male_day >= 14) or (male_month == 2 and male_day <= 12):
          Male_sign="Capricorn"

    #Aquarius: February 13 - March 13
    elif (male_month == 2 and male_day >= 13) or (male_month == 3 and male_day <= 13):
          Male_sign="Aquarius"

    #Pisces: March 14 - April 13
    else:
          Male_sign="Pisces"



female_day = int(input("Enter Day Of Birth(female) : "))
female_month = int(input("Enter Month Of Birth(female) : "))
print()

# Days in each month 
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if female_month < 1 or female_month > 12 or female_day < 1 or female_day > days_in_month[female_month -1]:
    print("Please Enter Valid Date Of Birth")
    exit()

else:
     #Aries: April 14 - May 14
    if (female_month == 4 and female_day >= 14) or (female_month == 5 and female_day <= 14):
          Female_sign="Aries"

    #Taurus: May 15 - June 14
    elif (female_month == 5 and female_day >= 15) or (female_month == 6 and female_day <= 14):
          Female_sign="Taurus"

    #Gemini: June 15 - July 16
    elif (female_month == 6 and female_day >= 15) or (female_month == 7 and female_day <= 16):
          Female_sign="Gemini"

    #Cancer: July 17 - August 16
    elif (female_month == 7 and female_day >= 17) or (female_month == 8 and female_day <= 16):
          Female_sign="Cancer"

    #Leo: August 17 - September 16
    elif (female_month == 8 and female_day >= 17) or (female_month == 9 and female_day <= 16):
          Female_sign="Leo"

    #Virgo: September 17 - October 16
    elif (female_month == 9 and female_day >= 17) or (female_month == 10 and female_day <= 16):
          Female_sign="Virgo"

    #Libra: October 17 - November 15
    elif (female_month == 10 and female_day >= 17) or (female_month == 11 and female_day <= 15):
          Female_sign="Libra"

    #Scorpio: November 16 - December 15
    elif (female_month == 11 and female_day >= 16) or (female_month == 12 and female_day <= 15):
          Female_sign="Scorpio"

    #Sagittarius: December 16 - January 13
    elif (female_month == 12 and female_day >= 16) or (female_month == 1 and female_day <= 13):
          Female_sign="Sagittarius"

    #Capricorn: January 14 - February 12
    elif (female_month == 1 and female_day >= 14) or (female_month == 2 and female_day <= 12):
          Female_sign="Capricorn"

    #Aquarius: February 13 - March 13
    elif (female_month == 2 and female_day >= 13) or (female_month == 3 and female_day <= 13):
          Female_sign="Aquarius"

    #Pisces: March 14 - April 13
    else:
          Female_sign="Pisces"

print("Male Zodiac Sign Is",Male_sign)
print()
print("Female Zodiac Sign Is",Female_sign)
print()

if Male_sign == "Aries":
    if Female_sign == "Aries" or Female_sign == "Leo" or Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Libra" or Female_sign == "Aquarius":
        print("Great Match")
    elif Female_sign == "Virgo" or Female_sign == "Pisces":
        print("Favorable Match")
    else:
        print("Not Favorable")

elif Male_sign == "Leo":
    if Female_sign == "Aries" or Female_sign == "Leo" or Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Libra":
        print("Great Match")
    elif Female_sign == "Virgo" or Female_sign == "Capricorn":
        print("Not Favorable")
    else:
        print("Favorable Match")

elif Male_sign == "Sagittarius":
    if Female_sign == "Aries" or Female_sign == "Leo" or Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Libra" or Female_sign == "Aquarius":
        print("Great Match")
    elif Female_sign == "Taurus" or Female_sign == "Virgo" or Female_sign == "Capricorn":
        print("Not Favorable")
    else:
        print("Favorable Match")

elif Male_sign == "Taurus":
    if Female_sign == "Aries" or Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Aquarius":
        print("Not Favorable")
    elif Female_sign == "Leo" or Female_sign == "Libra":
        print("Favorable Match")
    else:
        print("Great Match")

elif Male_sign == "Virgo":
    if Female_sign == "Leo" or Female_sign == "Aquarius":
        print("Favorable Match")
    elif Female_sign == "Aries" or Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Libra" or Female_sign == "Pisces":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Capricorn":
    if Female_sign == "Leo" or Female_sign == "Libra":
        print("Favorable Match")
    elif Female_sign == "Aries" or Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Aquarius":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Gemini":
    if Female_sign == "Sagittarius" or Female_sign == "Virgo" or Female_sign == "Capricorn":
        print("Favorable Match")
    elif Female_sign == "Taurus" or Female_sign == "Cancer" or Female_sign == "Scorpio" or Female_sign == "Pisces":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Libra":
    if Female_sign == "Aries" or Female_sign == "Taurus" or Female_sign == "Pisces":
        print("Favorable Match")
    elif Female_sign == "Virgo" or Female_sign == "Capricorn" or Female_sign == "Cancer" or Female_sign == "Scorpio":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Aquarius":
    if Female_sign == "Scorpio" or Female_sign == "Pisces":
        print("Favorable Match")
    elif Female_sign == "Taurus" or Female_sign == "Virgo" or Female_sign == "Capricorn" or Female_sign == "Cancer":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Cancer":
    if Female_sign == "Leo" or Female_sign == "Sagittarius":
        print("Favorable Match")
    elif Female_sign == "Aries" or Female_sign == "Gemini" or Female_sign == "Libra" or Female_sign == "Aquarius":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Scorpio":
    if Female_sign == "Aries" or Female_sign == "Leo":
        print("Favorable Match")
    elif Female_sign == "Sagittarius" or Female_sign == "Gemini" or Female_sign == "Libra" or Female_sign == "Aquarius":
        print("Not Favorable")
    else:
        print("Great Match")

elif Male_sign == "Pisces":
    if Female_sign == "Gemini" or Female_sign == "Libra" or Female_sign == "Aquarius":
        print("Not Favorable")
    elif Female_sign == "Aries" or Female_sign == "Leo" or Female_sign == "Sagittarius" or Female_sign == "Virgo":
        print("Favorable Match")
    else:
        print("Great Match")

print("Thank You")


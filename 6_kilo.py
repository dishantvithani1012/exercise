#write a program to accept grams from user, then calculate and display kilograms and remaining grams 

grams = int(input("Enter Grams : " ))

kilograms= grams //1000
remening_grams = grams %1000

print(f"{kilograms} Kilo And {remening_grams} Grams")
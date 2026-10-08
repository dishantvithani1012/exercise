#write a program to accept inches from user, then calculate and display feets and remaining inches

inches = int(input("Enter Inches :" ))
feets = inches //12
remainig_inches = inches % 12

print(f"{feets } Feet And {remainig_inches} Inch")

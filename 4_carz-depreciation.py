#write a program to calculate single line depreciation from user given car price, shelf life and wreckages price. 

car_price = float(input("Enter car price :"))
shelf_life = float(input("Enter car Shelf Life : "))
wreckages_price = float(input(" Enter car  Wreckages Price : "))

Annual_Depriciation = (car_price - wreckages_price )/shelf_life

print("Annual Depriciation of car is : ",Annual_Depriciation)
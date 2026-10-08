# gst amount and total amount 

amount = float(input("enter amount : "))
rate = float(input("Enter Rate : "))

gst =(amount* rate)/100
total_amount = amount + gst

print("Amount Is :",amount)
print("Rate Is :",rate)
print("Total Amount Is :",total_amount)


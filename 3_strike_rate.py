# write a program to calculate batter strike rate from user given runs and balls  
 
run = int(input("Enter the Run Scored by player : "))
balls = int(input("Enter the Balls Played by playes"))

strike_rate = (run/balls) * 100

print("Player Strike Rate is ",strike_rate)
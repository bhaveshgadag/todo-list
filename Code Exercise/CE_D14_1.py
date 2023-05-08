# Create a function that finds out the state of water (i.e., gas, liquid, solid) 
# given the temperature. In other words, the function has a temperature 
# parameter and returns either "Gas", "Liquid" or "Solid" as a string 
# depending on the temperature. The function should be written 
# in a separate file from the command line interface file.
# Note: To check if a value is between two values, 0 < x < 100:
	
import CE_D14_functions as functions

temperature = float(input("Enter temperature of water: "))

state = functions.state_of_water(temperature)

print(state)
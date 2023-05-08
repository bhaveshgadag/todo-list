# Module for CE_D14_1
#
# In coding exercise 1, we hardcoded the values 0 and 100. 
# It is better to change them to constants in the script where 
# the function is defined. Therefore, your task is to modify the 
#script from exercise 1 by creating two global variables/constants 
# in that file, one variable associated with 0 and another 
# associated with 100. Then, use those variables in the
# function instead of the values.

boiling_point = 100
freezing_point = 0

def state_of_water(temperature_local):
	""" Function to get state of water, gets temperature as
	 parameter, and returns either Solid, Liquid, or Gas."""
	if temperature_local <= freezing_point:
		state = 'Solid'
	elif temperature_local >= boiling_point:
		state = 'Gas'
	else:
		state = 'Liquid'
	
	return state
	

if __name__ == '__main__':
	temperature = 12
	print(f"Temperature : {temperature}")
	print(state_of_water(temperature))
	
	temperature = 102
	print(f"Temperature : {temperature}")
	print(state_of_water(temperature))
	
	temperature = -4
	print(f"Temperature : {temperature}")
	print(state_of_water(temperature))
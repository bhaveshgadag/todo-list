# Create a function that converts liters to cubic meters 
# knowing that 1000 liters make 1 cubic meter.

def liter_to_cubic(liters_local):
	cubic = liters_local / 1000
	return cubic
	
	
liters = float(input("Enter liters to convert into cubic meter : "))

cubic_meters = liter_to_cubic(liters)

print(f"{liters} liters is {cubic_meters} cubic meters.")
def parse(feet_inches_local):
	parsed_local = feet_inches_local.split(' ')
	feet = float(parsed_local[0])
	inch = float(parsed_local[1])
	return feet,inch


def convert(feet,inch):
	meters_local = feet * 0.3048 + inch * 0.0254
	return meters_local
	
	
feet_inches = input("Enter feet and inches to convert to meters")

parsed = parse(feet_inches)

meters = convert(parsed[0],parsed[1])

print(f"{parsed[0]} feet and {parsed[1]} inches is {meters} meters")



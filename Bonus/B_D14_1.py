from parsers import parse
from converters import convert

	
feet_inches = input("Enter feet and inches to convert to meters")

parsed = parse(feet_inches)

meters = convert(parsed[0],parsed[1])

print(f"{parsed[0]} feet and {parsed[1]} inches is {meters} meters")



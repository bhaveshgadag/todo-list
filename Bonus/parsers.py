# Module for B_D14_1

def parse(feet_inches_local):
	parsed_local = feet_inches_local.split(' ')
	feet = float(parsed_local[0])
	inch = float(parsed_local[1])
	return feet,inch
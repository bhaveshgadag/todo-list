# Get temperatures from a text file and calculate average of
# temperatures using function

def get_average():
	with open("../files/temperatures.txt",'r') as file:
		data = file.readlines()
	temps = data[1:]
	temps = [float(temp) for temp in temps]
	
	average_local = sum(temps)/len(temps)
	
	return average_local

average = get_average()
print(average)
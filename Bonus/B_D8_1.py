date = input("Enter today's date:")
mood = input("Rate your mood for today from 1 to 10 :")
thought = input("Your thoughts for today\n")

with open(f"../Journal/{date}.txt", 'w') as file:
	file.write(f'Mood : {mood}  \n')
	file.write("Thoughts :\n" + thought)
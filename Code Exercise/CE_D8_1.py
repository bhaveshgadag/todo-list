# A client wants to buy a coin-flip probability program from you.
# The programs should work like this:
# 1. The user runs the program.
# The program asks the user to enter "head" or "tail". 
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". 
# The user does the same over and over again.

#	Throw the coin and enter head or tail here? tail
#	Heads: 0.0%
#	Throw the coin and enter head or tail here? head
#	Heads: 50.0%
#	Throw the coin and enter head or tail here? head
#	Heads: 66.666666%
#	Throw the coin and enter head or tail here? tail
#	Heads: 50.0%
#	Throw the coin and enter head or tail here? tail

# In each cycle, the program should return the current percentage of heads in the program.
# Also, you should write each user entry (i.e., head or tail) in a text file using a with-context manager, one entry per line.

while True:
	filename = "coin_flip_probability.txt"
	coin_face = input("Throw the coin and enter head or tail here? ") + "\n"
	
	if coin_face == 'exit\n':
		break
		
	with open(filename, 'r') as file:
		coin_flip_result = file.readlines()
		coin_flip_result.append(coin_face)
		
	with open(filename, 'w') as file:
		file.writelines(coin_flip_result)
		
	print(coin_flip_result)
		
	heads_probability = (coin_flip_result.count('head\n') / len(coin_flip_result)) * 100
	print(f"Heads: {heads_probability}%")
	
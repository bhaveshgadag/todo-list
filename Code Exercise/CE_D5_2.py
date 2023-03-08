# ips = ['100.122.133.105', '100.122.133.111']
#
# Copy-paste the ips list in a .py file and extend the program so it:
#
# 1. Prompts the user to input an index (e.g, 0 or 1).
#
# 2. Returns the IP address that has that index.
#
# Here is how the program would behave when executed:
#
# Enter the index of the IP you want: 1
# You choose 100.122.133.111

ips = ['100.122.133.105', '100.122.133.111']

index = int(input("Enter the index of the IP you want: "))

print(f"You choose {ips[index]}")

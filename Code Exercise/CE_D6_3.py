# Please download the members.txt file from the resources of this article.
# Then, create a program that, whenever executed,
# asks the user to enter a new member in the command line:
# 	Add a new member: Solomon Right
# Then, the member is added to members.txt.
# In this case, the text file content would be:
# 	John Smith
# 	Sen Lakmi
# 	Sono Octonot
# 	Solomon Right

file = open("../files/members.txt", 'r')
members = file.readlines()
file.close()

new_member = input("Add a new member: ") + "\n"

members.append(new_member)

file = open("../files/members.txt", 'w')
file.writelines(members)
file.close()
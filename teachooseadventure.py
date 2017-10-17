print("""You are invited to your own coronation.
Do you get crowned in England or Spain? For England, type 1; for Spain, type 2.""")

country = input("> ")

if country == "1":  
	print("There's been a bit of conflict in England. Too many people have gotten tipsy from their tea.")
	print("What do you do? Please type 1 or 2:")
	print("1. Outlaw tea.")
	print("2. Restrict tea for your royal consumption only.")

tea_action = input("> ")

if tea_action == "1":
	print("Uh-oh. There's been a Revolution. Seems your actions have not been welcomed.")
elif tea_action ==  "2":
	print( "Nice move. Seems you're royally great at imperialism.")

if country == "2":
	print("There's unrest in Madrid. Seems people want to dance flamenco all day and not work.")
	print("What do you do?")
	print("1. Join them dancing!")
	print("2. Offer extra chocolate if they take a siesta.")

jolly_action = input("> ")

if jolly_action == "1": 
	print("You can't lose with these options!")
	print("Good job!")

elif jolly_action == "2":
	print("You can't lose with these options!")
	print("Good job!")
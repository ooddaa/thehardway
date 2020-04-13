from sys import exit

def gold_room():
	print("This is gold room")
	choice = input('I take > ')
	print(f"choice is {choice}")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number")

	if how_much < 50:
		print("Good job, you aren't as greedy as those corpses over there, you can go.")
		exit(0)
	else:
		dead("Naughty, naughty, pile_of_corpses++")

def bear_room():
	print("This is bear room, your action?")
	print("1. taunt bear")
	print("2. shout at bear")
	bear_moved = False

	while True:
		action = input("> ")

		if action == "taunt bear" or action == "1"  and not bear_moved:
			print("Smart move! Bear has moved and you see a door behind it!")
			print("Want to go there?")
			bear_moved = True
			if input("yes/no > ") == "yes":
				gold_room()
			else:
				print("ok, don't go there then, it's only gold there, after all, the point of the game...")
		elif action == "shout at bear" or action == "2":
			print("This particular bear is quite sensitive to sudden loud noises and tends to chew limbs off the emmiter, which is, in this case, you.")
			dead("Not much there left for you to do without limbs and all that blood spilled around...")
		else:
			print("You sure? If you don't do one of the options, you'll waste all your time here...")
			ans = input("y/n > ")
			if ans == "y":
				dead("You died old, standing there.")
			bear_room()

def cthulhu_room():
	print("This is good old Cthulhu room, welcome back!")
	action = input("action > ")
	
	if action == "flee":
		start()
	else:
		dead("You should've fled, mate.")

def dead(why):
	print(f"{why}. You are dead. Good job!")
	exit(0)

def start():
	print("You are in a room with two doors - left and right")
	print("Which one you take?")
	door = input("> ")

	if door == "left":
		bear_room()
	elif door == "right":
		cthulhu_room()
	else:
		print("Dude, don't test my patience.")
		start()
start()

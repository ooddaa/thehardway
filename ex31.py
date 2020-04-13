'''from sys import argv

script, val = argv
val = int(val)
'''
print("""
You enter a dark room with two doors.
Do you go through door № 1or door №2?
""")
door = input("> ")

if door == '1':
	print(f"There's a giant bear here eating a cheese cake.")
	print(f"What do you do?")
	print("1. Take the cake.")
	print("2. Apologise and close the door.")

	action = input('> ')
	
	if action == '1':
		print(f"Very courageous but also extremely stupid - the bear bites your leg off.")
	elif action == '2':
		print(f"Good choice!")
	else:
		print(f"Well, doing {action} worked magic - the bear got scared and ran off!")

elif door == '2':
	print(f"Staring into the endless abyss of a Cthulhu's retina.")
	print("1. Strawberries")
	print("2. Strawberries devided by zero smell")
	print("3. Understanding modern nordic music")
	
	insanity = input('> ')
	
	if insanity == '1':
		print("Your mind narrowly survives Cthulhu's stare due to extra vitamin C from strawberries")
		print("Well done!")
	elif insanity == '2':
		print("Insanity melts your brains into a jelly")
		print("Bad choice!")
	elif insanity == '3':
		print("Wow it's just not to Cthulhu's liking, and it's shrinking in size to evaporate completely.\nYou won!")
	else:
		print("Whops, nothing happened, except that you will stay here forever vis-a-vis with Cthulhu's bad breath.")
else:
	print(f"There is no door №{door}. Have a great flight!")

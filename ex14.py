from sys import argv

script, user_name, password = argv
prompt = '> '

print(f'Hi {user_name}, I\'m the {script} script')
print(f"I'd like to ask you a few questions")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Ok, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

print("Do you want to see something really interesting?")
ans = input('yes/no ')
if ans == 'yes':
	print(f"Me, being a superb script, have already hacked your password!, it's {password} !! Mhaha")
else:
	print(f"No one wants to play with me...")

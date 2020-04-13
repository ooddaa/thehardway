from sys import argv 

script, people, cars, trucks = argv
"""
people = 20
cars = 23
trucks = 15
"""
print(f"{people} people, {cars} cars, {trucks} trucks")
if people > cars:
	print("Not enough cars for people")
elif people < cars:
	print("We can just take cars")
else:
	print("Hmmm, there appears to be as many cars as people...")

if trucks > cars:
	print("More trucks then cars")
elif trucks < cars:
	print("Less trucks then cars")
else:
	print("the only option left is trucks == cars")

if people > trucks:
	print("More people then trucks")
elif people < trucks:
	print("Less people then trucks")
else:
	print("enough of it")


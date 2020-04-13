from sys import argv

script, filename = argv

print(f"Hi, I'm {script} and now I'm gonna load {filename}")
file = open(filename)

print(f"Here is your file")
print(file.read())
file.close()
print("Do you want to read another?")
another_file = input('> ')

print("Here you go:")
print(open(another_file).read())
another_file.close()

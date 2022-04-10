from sys import argv

script, filename = argv

print(f"Now we're going to empty {filename}")
print("Do you want that? Hit CTRL-C (^C) if 'no'")
print("Hit RETURN if 'yes'")

input('> ')
file = open(filename, 'w')
print(f"OK, let's empty it then")
file.truncate()

print("Now, I'll ask you for 3 new lines")

line1 = input('Line 1: ')
line2 = input('Line 2: ')
line3 = input('Line 3: ')

file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")

print(f"Is it there?")
answer = input('(y)/(N)> ')
# if answer == 'y' or 'Y' or '(y)' or 'yes':
if answer == 'y' or answer == 'Y' or answer == '(y)' or answer == 'yes':
    print('all ok, thanks')
    file.close()
    # newF = open(filename)
    # print(newF.read())
else:
    print('I didn\'t expect that. Not implemented. closing down')
    file.close()

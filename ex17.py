from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Now we'll copy stuff from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
#print(f"Does output file exist? {exists(to_file)}")
#print(f"If ready, hit RETURN, else hit CTRL-C")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

print(f"All copied")

in_file.close()
out_file.close()

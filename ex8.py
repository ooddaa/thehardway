formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"если горит твоя изба",
	"значит всему твоему пизда", 
	"если изба твоя горит -", 
	"это прямо с тобой бог говорит",
))

print("lets practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = '''
\t если горит твоя изба
значит всему твоему пизда
\t если изба твоя горит
это с тобой бог говорит.
\nбог говорит: \nслышь, чувачок,
ты вот как-то не очень ок.
\nбог говорит: \nау, братиш, 
делись поровней и будь потиш
'''

print("-------------------") 
print(poem)
print("-------------------")

five = 10 / 2
print(f"{five} is five")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print('our starting point is {}'.format(start_point))
print(f'We have {beans} beans, {jars} jars, {crates} crates')

start_point = start_point / 10

print('This will also work:')
formula = secret_formula(start_point)
print('We have {} beans, {} jars, {} crates'.format(*formula))

from LettersClock import letters_clock as lc

emblem = {
	'SPACE': 'Gorilla',
	'LAND': 'Panda',
	'WATER': 'Octopus',
	'ICE': 'Mammoth',
	'AIR': 'Owl',
	'FIRE': 'Dragon'
}

def decrypt(planet, message):
	move_backward_by = len(emblem[planet])
	
	for i in message:
		for node in lc:
			if i == node.value:
				summa = 0
				for k in lc.move_backward(node):
					if move_backward_by == summa:
						print(k.value);
						break
					summa += 1
						
						
decrypt('ICE', 'STHSTSTVSASOS')
from LettersClock import letters_clock as lc
from LettersClock import letters
from BinarySearch import find_index

emblem = {
	'SPACE': 'Gorilla',
	'LAND': 'Panda',
	'WATER': 'Octopus',
	'ICE': 'Mammoth',
	'AIR': 'Owl',
	'FIRE': 'Dragon'
}

def forward_or_backward(letter, pos):
	index = find_index(letters, letter)
	if index > pos:
		return 'forward'
	elif index < pos:
		return 'backward'
	else:
		return 'stay'
		
		
def move_backward_by(node, move_by):
	i = 0
	for node in lc.move_backward(node):
		if i == move_by:
			return node
		i += 1

def decrypt(planet, message):
	move_by = len(emblem[planet])
	pos = 0
	move_from = lc.root
	result = ''
	
	for letter in message:
		if pos < 0:
			pos = 26 + pos
		
		go = forward_or_backward(letter, pos)
		
		if go == 'forward':
			for node in lc.move_forward(move_from):
				if node.value == letter.upper():
					desired = move_backward_by(node, move_by)
					result += desired.value
					
					pos -= move_by
					move_from = desired
					break
				else:
					pos += 1
					
		elif go == 'backward':
			for node in lc.move_backward(move_from):
				if node.value == letter.upper():
					desired = move_backward_by(node, move_by)
					result += desired.value
					
					pos -= move_by
					move_from = desired
					break
				else:
					pos -= 1
					
		else:
			desired = move_backward_by(move_from, move_by)
			result += desired.value
	
	return result
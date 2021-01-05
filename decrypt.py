from letters_clock import letters, letters_clock as lc
from binary_search import find_index
from emblem import emblem
from circular_ll import Root

output = {
	'SPACE': {},
	'LAND': {},
	'WATER': {},
	'ICE': {},
	'AIR': {},
	'FIRE': {}
}

def forward_or_backward(letter, pos):
	"""
		@params - letter and current position on letters clock
		returns forward, backward and stay based on the index returned
		from find_index function
	"""
	
	# find_index function will perform binary search on letters list
	index = find_index(letters, letter)
	
	if index > pos:
		return 'forward'
	elif index < pos:
		return 'backward'
	else:
		return 'stay'
		
		
def move_backward_by(node, move_by):
	"""
		Takes current node on the letters clock and move_by(int),
		move backward on letters clock by (move_by) position and returns the node
	"""
	
	i = 0
	for node in lc.move_backward(node):
		if i == move_by:
			return node
		i += 1
		
def update_output(kingdom, value):
	"""
		@params - kingdom(string) and value(string)
		updates increment output[kindom][value] or create one with number of occurrences of value
	"""
	
	try:
		output[kingdom][value] += 1
	except KeyError:
		output[kingdom][value] = 1

def decrypt(kingdom, message):
	"""
		@params - kingdom and message to decrypt
		Returns list of decrypted message and output dict
		output dict - will contain number of occurrences of every letters in decrypted message
	"""
	
	# move_by 
	move_by = len(emblem[kingdom])
	
	# pos and move_from tracks current node in letters clock
	pos = 0
	move_from = lc.root
	
	# will hold decrypted message
	result = ''
	
	# iterates through every letters in message
	# and decrypts every letter using letters_clock
	for letter in message:
		if pos < 0:
			pos = len(letters) + pos
		
		# decides whether to go forward or backward in letters_clock,
		# using letter and current position(pos) in letters_clock
		go = forward_or_backward(letter, pos)
		
		if go == 'forward':
			
			# search clockwise for letter on letters_clock from move_from(node)
			for node in lc.move_forward(move_from):
				if node.value == letter.upper():
					# decrypt letter
					desired = move_backward_by(node, move_by)
					
					# update result and output with decrypted letter
					result += desired.value
					update_output(kingdom, desired.value)
					
					# track the letters_clock
					pos -= move_by
					move_from = desired
					
					break
				
				# updates position for every move on letters_clock
				pos += 1
					
		elif go == 'backward':
			
			# search anticlockwise for letter on letters_clock from move_from(node)
			for node in lc.move_backward(move_from):
				if node.value == letter.upper():
					# decrypt letter
					desired = move_backward_by(node, move_by)
					
					# update result and output with decrypted letter
					result += desired.value
					update_output(kingdom, desired.value)
					
					# track the letters_clock
					pos -= move_by
					move_from = desired
					
					break
					
				# updates position for every move on letters_clock
				pos -= 1
					
		else:
			# no need for search, the current node is what we are looking for
			
			# decrypt letter
			desired = move_backward_by(move_from, move_by)
			
			# update result and output with decrypted value
			result += desired.value
			update_output(kingdom, desired.value)
	
	return [result, output]
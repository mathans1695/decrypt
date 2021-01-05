from circular_ll import Root

emblem = {
	'SPACE': 'Gorilla',
	'LAND': 'Panda',
	'WATER': 'Octopus',
	'ICE': 'Mammoth',
	'AIR': 'Owl',
	'FIRE': 'Dragon'
}

# expected will contain number of occurrences of letters in emblem for each kingdom
expected = {
	'SPACE': {},
	'LAND': {},
	'WATER': {},
	'ICE': {},
	'AIR': {},
	'FIRE': {}
}

def generate_expected_result(kindom, emblem):
	"""
		updates expected with number of occurences of letters in emblem
		@params - kindom, corresponding emblem
	"""
	for letter in emblem:
		try:
			expected[kindom][letter.upper()] += 1
		except KeyError:
			expected[kindom][letter.upper()] = 1
	
for key in emblem:
	generate_expected_result(key, emblem[key])
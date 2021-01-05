from CircularLL import Root

emblem = {
	'SPACE': 'Gorilla',
	'LAND': 'Panda',
	'WATER': 'Octopus',
	'ICE': 'Mammoth',
	'AIR': 'Owl',
	'FIRE': 'Dragon'
}

expected = {
	'SPACE': {},
	'LAND': {},
	'WATER': {},
	'ICE': {},
	'AIR': {},
	'FIRE': {}
}

def generate_expected_result(planet, symbol):
	for letter in symbol:
		try:
			expected[planet][letter.upper()] += 1
		except KeyError:
			expected[planet][letter.upper()] = 1
	
for key in emblem:
	generate_expected_result(key, emblem[key])
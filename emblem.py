from CircularLL import Root

emblem = {
	'SPACE': 'Gorilla',
	'LAND': 'Panda',
	'WATER': 'Octopus',
	'ICE': 'Mammoth',
	'AIR': 'Owl',
	'FIRE': 'Dragon'
}

expected = {}

def generate_expected_result(key, value):
	letters_list = Root(value[0])
	
	for i in range(1, len(value)):
		letters_list.push(value[i])
		
	expected[key] = letters_list
	
for key in emblem:
	generate_expected_result(key, emblem[key])
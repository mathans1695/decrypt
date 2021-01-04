from CircularLL import Root	
		   
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
		   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
		   'Y', 'Z']

letters_clock = Root(letters[0])

for i in range(1, len(letters)):
	letters_clock.push(letters[i])
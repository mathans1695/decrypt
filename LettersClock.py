from CircularLL import Root	
		   
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letters_clock = Root(letters[0])

for i in range(1, len(letters)):
	letters_clock.insert('', letters[i])
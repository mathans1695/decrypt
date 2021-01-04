from CircularLL import Root	
		   
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZAA'

letters_clock = Root(letters[0])

for i in range(1, len(letters)):
	letters_clock.push(letters[i])
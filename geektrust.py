from decrypt import decrypt
from emblem import expected
import sys

def compare_with_expected(planet, decrypt_dict):
	count = 0
	
	for letter in expected[planet]:
		try:
			if decrypt_dict[planet][letter] >= expected[planet][letter]:
				count += 1
		except KeyError:
			pass
			
	if count >= len(expected[planet]):
		return True
	return False

def main():
	with open(sys.argv[1], 'r') as f:
		inp = f.read()

	decrypted = None
	decrypt_dict = None
	output = ''
	possible_no_of_alliance = 0

	for splitted in [j.split(' ') for j in inp.split('\n')]:
		if len(splitted) > 2:
			join = ''
			for j in range(1, len(splitted)):
				join += splitted[j]
			decrypted, decrypt_dict = decrypt(splitted[0], join)
		else:
			decrypted, decrypt_dict = decrypt(splitted[0], splitted[1])
	
		if compare_with_expected(splitted[0], decrypt_dict):
			output += splitted[0] + ' '
			possible_no_of_alliance += 1
		
	if possible_no_of_alliance >= 3:
		temp = 'SPACE '
		output = temp + output
	else:
		output = 'NONE'
	
	print(output.strip())

if __name__ == "__main__":
	main()
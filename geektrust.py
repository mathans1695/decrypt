from decrypt import decrypt
from emblem import expected
import sys

def compare_with_expected(kingdom, decrypted_dict):
	"""
		Compare decrypted dictionary with expected dictionary based on kingdom
		Returns True, if decrypted dictionary atleast have expected dictionary letters occurrences
		Returns False, if decrypted dictionary doesn't match expected dictionary letters occurrences
	"""

	count = 0
	for letter in expected[kingdom]:
		try:
			if decrypted_dict[kingdom][letter] >= expected[kingdom][letter]:
				count += 1
		except KeyError:
			pass
			
	if count >= len(expected[kingdom]):
		return True
	return False

def main():
	
	# Read input file and store it in inp
	with open(sys.argv[1], 'r') as f:
		inp = f.read()
	
	output = ''
	possible_no_of_alliance = 0
	
	# splits the input and iterate
	for splitted in [j.split(' ') for j in inp.split('\n')]:
		kingdom, message = splitted[0], splitted[1]
		
		# remove spaces in message
		if len(splitted) > 2:
			message = ''
			for j in range(1, len(splitted)):
				message += splitted[j]
				
			decrypted, decrypted_dict = decrypt(kingdom, message)
		else:
			decrypted, decrypted_dict = decrypt(kingdom, message)
		
		# increment alliance and concat the kingdom to output string
		if compare_with_expected(kingdom, decrypted_dict):
			output += splitted[0] + ' '
			possible_no_of_alliance += 1
	
	# if king atleast have three alliance, concatenate space to output in front
	if possible_no_of_alliance >= 3:
		temp = 'SPACE '
		output = temp + output
	else:
		output = 'NONE'
	
	print(output.strip())

if __name__ == "__main__":
	main()
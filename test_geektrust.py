import unittest
from geektrust import main, compare_with_expected
import sys

class TestGeekTrust(unittest.TestCase):
	def test_compare_with_expected(self):
		# Arrange
		decrypted_dict = {
			'AIR': {'O': 1, 'W': 1, 'L': 1}
		}
		
		# should return true
		# if both decrypted and expected dict occurrences atleast match each other
		self.assertTrue(compare_with_expected('AIR', decrypted_dict))
		
	def test_main(self):
		# Provide path to input file, while excecuting the program
		
		# should return 'SPACE LAND ICE FIRE', if condition satisfied
		sys.argv.append('success_data.txt')
		self.assertEqual(main(), "SPACE LAND ICE FIRE")
		
		sys.argv.pop()
		
		# should return 'NONE', if condition not satisfied
		sys.argv.append('failure_data.txt')
		self.assertEqual(main(), "NONE")
		
if __name__ == "__main__":
	unittest.main()
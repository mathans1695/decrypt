import unittest
import decrypt
from letters_clock import letters_clock as lc

class TestDecrypt(unittest.TestCase):
	def test_forward_or_backward(self):
		# should return forward - 'N' is at index 13, which is greater than 5
		self.assertEqual(decrypt.forward_or_backward('N', 5), 'forward')
		
		# should return backward - 'N' is at index 23, which is less than 13
		self.assertEqual(decrypt.forward_or_backward('N', 23), 'backward')
		
		# should return stay - 'N' is at index 13, which is equal to 13
		self.assertEqual(decrypt.forward_or_backward('N', 13), 'stay')
		
	def test_move_backward_by(self):
		# should move certain steps backward from provided node
		
		# should return node 'X' from node 'Z', if move_by == 3
		self.assertEqual(decrypt.move_backward_by(lc.root, 3).value, 'X')
		
	def test_decrypt(self):
		# should decrypt the provided message
		
		# should return 'AABC', if 'DDEF' provided as input
		decrypted, decrypted_dict = decrypt.decrypt('AIR', 'DDEF')
		self.assertEqual(decrypted, 'AABC')
		 
		# 'A' occurs twice
		self.assertEqual(decrypted_dict['AIR']['A'], 2)
		# 'B' occurs once
		self.assertEqual(decrypted_dict['AIR']['B'], 1)
		# 'C' occurs once
		self.assertEqual(decrypted_dict['AIR']['C'], 1)
		
		
if __name__ == "__main__":
	unittest.main()
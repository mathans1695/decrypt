import unittest
from binary_search import find_index

class TestBinarySearch(unittest.TestCase):
	def setUp(self):
		# Arrange
		self.array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
				 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
				 'U', 'V', 'W', 'X', 'Y', 'Z']

	def test_find_index(self):
		# returns index, if value found in the array
		# first test
		self.assertEqual(find_index(self.array, 'B'), 1)
		
		# second test 
		self.assertEqual(find_index(self.array, 'S'), 18)
		
		# returns None, if value not found in the array
		self.assertEqual(find_index(self.array, 'haha'), None)
		
	def test_find_index_value(self):
		# raise attribute error, if int or float value passed to find_index
		
		with self.assertRaises(AttributeError):
			find_index(find_index(self.array, 1))
			
	def tearDown(self):
		self.array = None
	
	
if __name__ == "__main__":
	unittest.main()
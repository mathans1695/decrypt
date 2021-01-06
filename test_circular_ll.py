import unittest
from circular_ll import Root

class TestCircularLinkedList(unittest.TestCase):
	def setUp(self):
		self.root = Root('A')
		
	def test_push(self):
		# should add new node to linked list
		
		# add new node
		self.root.push('B')
		
		# linked list length should be 2
		self.assertEqual(len(self.root), 2)
		
		# 'B' should be added to linked list
		for i in range(len(self.root)):
			if i == 1:
				self.assertEqual('B', 'B')
				
	def test_move_forward_method(self):
		# should go forward in linked list
		# Arrange
		root = self.root
		
		# add five nodes to linked list
		for value in ['B', 'C', 'D', 'E', 'F']:
			root.push(value)
			
		# go forward through ll from root node
		expected1 = ''
		for node in root.move_forward(root.root):
			expected1 += node.value
		self.assertEqual(expected1, 'ABCDEF')
		
		# start from third node and go forward
		expected2 = ''
		for node in root.move_forward(root.root.next.next):
			expected2 += node.value
		self.assertEqual(expected2, 'CDEFAB')
		
	def test_move_backward_method(self):
		# should go backword in linked list
		# Arrange
		root = self.root
		
		# add five nodes to linked list
		for value in ['B', 'C', 'D', 'E', 'F']:
			root.push(value)
			
		# go forward through ll from root node
		expected1 = ''
		for node in root.move_backward(root.root):
			expected1 += node.value
		self.assertEqual(expected1, 'AFEDCB')
		
		# start from last node and go forward
		expected2 = ''
		for node in root.move_backward(root.root.previous):
			expected2 += node.value
		self.assertEqual(expected2, 'FEDCBA')
		
				
	def tearDown(self):
		self.root = None
		
if __name__ == "__main__":
	unittest.main()
class Node:
	""" Creates single node """
	def __init__(self, value):
		self.previous = None
		self.value = value
		self.next = None
		self.count = 1

class Root:
	def __init__(self, value):
		self.root = Node(value.upper())
		self.current = self.root
		self.length = 1
		
	def push(self, value):
		""" 
			Create new node with value and push the node at the end, if linkedlist doesn't have one
			Or update the count property of node having the value passed as params
		"""
		
		i = 1
		
		# iterate through linkedlist and create new node or update count property
		for node in self:
			if node.value == value.upper():
				node.count += 1
				return True
				
			else:
				if self.length == 1:
					new = Node(value.upper())
					new.next = self.root
					new.previous = self.root
					
					self.root.next = new
					self.root.previous = new
					
					self.length += 1 
					return True
		
				if self.length == i:
					new = Node(value.upper())
					new.previous = node
					new.next = self.root
				
					node.next = new
					self.root.previous = new
					
					self.length += 1 
					return True
				
			i += 1
				
	def	move_forward(self, node):
		""" 
			Returns ForwardIterator
			Pass - Current node and length of linkedlist
		"""
		return ForwardIterator(node, self.length)
		
	def move_backward(self, node):
		""" 
			Returns BackwardIterator
			Pass - Current node and length of linkedlist
		"""
		return BackwardIterator(node, self.length)
		
	def __iter__(self):
		""" Returns LinkedListIterator iterator """
		return LinkedListIterator(self.root, self.length)
		
	def __len__(self):
		return self.length
			
class LinkedListIterator:
	""" Start clockwise iteration from root node """
	
	def __init__(self, root, length):
		self.current = root
		self.length = length
	
	def __iter__(self):
		return self
		
	def __next__(self):
		if self.length > 0:
			current = self.current
			self.current = current.next
			self.length -= 1
			return current
		else:
			raise StopIteration

class ForwardIterator:
	""" Perform clockwise iteration from passed node """
	
	def __init__(self, root, length):
		self.current = root
		self.length = length
	
	def __iter__(self):
		return self;
		
	def __next__(self):
		if self.length > 0:
			current = self.current
			self.current = current.next
			self.length -= 1
			return current
		else:
			raise StopIteration

class BackwardIterator:
	""" Perform anticlockwise iteration from passed node """
	
	def __init__(self, root, length):
		self.current = root
		self.length = length
	
	def __iter__(self):
		return self;
		
	def __next__(self):
		if self.length > 0:
			current = self.current 
			self.current = current.previous
			self.length -= 1
			return current
		else:
			raise StopIteration
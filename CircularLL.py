class Node:
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
		new = Node(value.upper())
		i = 1
		
		for node in self:
			if node.value == value.upper():
				node.count += 1
				return True
				
			else:
				if self.length == 1:
					new.next = self.root
					new.previous = self.root
					
					self.root.next = new
					self.root.previous = new
					
					self.length += 1 
					return True
		
				if self.length == i:
					new.previous = node
					new.next = self.root
				
					node.next = new
					self.root.previous = new
					
					self.length += 1 
					return True
				
			i += 1
				
	def	move_forward(self, node):
		return Forward_iterator(node, self.length)
		
	def move_backward(self, node):
		return Backward_iterator(node, self.length)
				
	def __iter__(self):
		return LinkedList_iterator(self.root, self.length);
			
class LinkedList_iterator:
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

class Forward_iterator:
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

class Backward_iterator:
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
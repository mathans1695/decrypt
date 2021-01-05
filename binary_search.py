from letters_clock import letters

def binary_search(arr, value):
	"""Perform binary_search on arr using value
	   Returns index, if value present in the list
	   Throw TypeError, if value not present in the list"""
			
	length = len(arr)
	mid = length // 2
	
	if mid == 0:
		if arr[mid] == value.upper():
			return mid
		return None
	
	if arr[mid] == value.upper():
		return mid
	
	elif arr[mid] > value.upper():
		return binary_search(arr[:mid], value)
	
	else:
		return mid + binary_search(arr[mid+1:], value) + 1

def find_index(arr, value):
	"""Returns the index of value from arr passed as parameters"""
	
	try:
		return binary_search(arr, value)
	except TypeError:
		return None
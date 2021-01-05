from letters_clock import letters

def binary_search(arr, value):
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
	try:
		return binary_search(arr, value)
	except TypeError:
		return None
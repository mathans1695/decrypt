def binary_search(arr, value):
	length = len(arr)
	mid = length // 2
	
	try:
		arr[mid]
	except IndexError:
		return 0
	
	if arr[mid] == value:
		return mid
	
	elif arr[mid] > value:
		return binary_search(arr[:mid], value)
	
	else:
		return mid + binary_search(arr[mid+1:], value) + 1

def find_index(arr, value):
	index = binary_search(arr, value)
	length = len(arr)
	
	if(length == index):
		return None
	else:
		return index
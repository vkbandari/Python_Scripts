'''
--------------------day01 : 25-01-21-------------
'''
# Linear Search Program------------------------------------------
def linear_search(array, search_element):
	'''
		* This function is to search element linearly in unsorted order.
		* Returns true if present else false.
	'''
	for inc in array:
		if inc == search_element:
			return True
	else:
		return False
	
	# end of function.
	
if __name__ == '__main__':
	'''
	  consider input: 
	  first line array	: 2 3 56 86 23 45 67 90 0
	  second line		: case1 : 45
				  case2 : 969 
	'''
	# input1 array with space separated in string form to list then int conversion.
	input_array = list(map(int, input("Enter array elements : ").split()))

	# input2 search element
	search_element = int(input("Enter search element : "))

	# function call
	Result = linear_search(input_array, search_element)

	# printing message based on returned result 
	if Result:
	  print("Hurrah..!!\n\t Searched element is present.")
	else:
	  print("Sorry..!!\n\t Searched element is not present.")



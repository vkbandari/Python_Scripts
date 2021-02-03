'''
--------------------day02 : 26-01-21-------------
'''  
# Binary Search Program------------------------------------------
# import time
def binary_search(array, search_element):
  '''
		* This function is to search element in sorted array with technique 
		of comparison fails split then comparison fails split until finding the
		search element or element not found.
		* Returns True, if element is present else False.
  '''
  # intializing left and  right indexes
  left_index = 0
  right_index = len(array)-1
  step = 1
  # loop until two things happen- 1. element find 2. middle index crosses right index
  while True:
                # print(f'step ={step} left = {left_index} right = {right_index}', end = '')

                # calculating middle index
                middle_index = (left_index + right_index) // 2
                # print(f' middle = {middle_index}')
                step += 1
                
                # Condition to trigger out of loop when middle index crosses right_index
                if middle_index > right_index:
                        return False
                # condtion to check present or not
                # print(f'\t {search_element} == {array[middle_index]}')
                if search_element == array[middle_index]:
                        return True

                # when search_element is less than 	middle_index, then it present in right side so
                elif search_element < array[middle_index]:
                        right_index = middle_index - 1

                # else left side only
                else:
                        left_index = middle_index + 1

                # time.sleep(5)
	
if __name__ == '__main__':       
        '''
                considering input:
                first line sorted array	: 12 26 35 84 96 123 265 965
                second line		: case1 : -56
                                          case2 : 123
        '''
        # input1 sorted array with space separated in string form to list then int conversion.
        input_sort_array = list(map(int, input("Enter array elements in sorted form : ").split()))

        # inp = '12 26 35 84 96 123 265 965'
        # input_sort_array = list(map(int, inp.split()))
        print(f'input array : {input_sort_array}')

        # input2 search element
        search_element = int(input("Enter Search element : "))

        # function call
        result = binary_search(input_sort_array, search_element)

        # printing message based on returned result
        if result:
                print("Hurrah..!!\n\t Searched element is present.")
        else:
                print("Sorry..!!\n\t Searched element is not present")
                


'''
--------------------day05 : 03-02-21-------------
'''
# triangle patterns

def pyramid_single_triangle():
    '''
        trying to print pattern like:
                *
               ***
              *****
    '''
    print(f'\n{"-"*70}')
    
    # input
    rows = int(input('Enter number of rows for single triangle : '))

    '''
    # old concept.
    for row in range(rows):
        for space in range(rows - row - 1):
            print(' ',end = '')
        for symbol in range(row * 2 + 1):
            print('*', end='')
        print()
    '''
    
    
    # first print spaces then symbols
    for row in range(rows):
        print(' ' * (rows - row - 1) + '*' * (row * 2 + 1))

    # for stem
    for _ in range(rows//2):
        # finding centre, based on that printing stems of 5 - #
        print(' ' * (rows - rows//4 -1) + '#' * (rows//2 + 1))

    # end of pyramid_triangle function.



def pyramid_multiple_triangles():
    '''
        same logic but multiple triangles one after another.
    '''
    print(f'\n{"-"*70}')

    # input of triangles count.
    tri_count = int(input('Enter number of triangles needed : '))

    # taking choice from the user.
    choice = int(input('choose \n\t0 - fixed size triangles \n\t1 - different user sizes \n\n\t\t input : '))

    print(f'\n{"-"*70}')
    if choice == 1:
        # empty list to store sizes from user_input
        input_list = []

        for _ in range(tri_count):
            input_list.append(int(input(f'\nEnter {_+1} triangle row size : ')))

        # Printing triangles based on list values
        for rows in input_list:
            for row in range(rows):
                print(' ' * (rows - row - 1) + '*' * (row * 2 + 1))

    elif choice == 0:
        # taking input - fixed size value.
        fixed_size = int(input('Enter fixed size for all triangles : '))

        # looping over triangles count
        for _ in range(tri_count):
            for row in range(fixed_size):
                print(' ' * (fixed_size - row - 1) + '*' * (row * 2 + 1))
    else:
        print('Invalid choice, Please try again....!!!!')
        
    # end of pyramid_multiple_triangles function.




if __name__ == '__main__':

    # choice from user
    choice = int(input('Choose \n\t1 - single triangle \n\t2 - multiple triangles \n\n\t\t input : '))

    if choice == 1:            
        # function call - single triangle
        pyramid_single_triangle()

    elif choice == 2:            
        #function call
        pyramid_multiple_triangles()

    else:
        print('Invalid choice, Please check the input...')
    


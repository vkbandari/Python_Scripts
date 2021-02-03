'''
--------------------day04 : 02-02-21-------------
'''
# find the traces of characters present or not

def char_trace(lista, listb):
    '''
        check based on positional, any traces or not.
        :return - if any char trace present return 'yes', else 'no'.
    '''
    temp_list = []
    for i, j in zip(lista, listb):
        for k in i:
            if k in j:
                temp_list.append('Yes')
                break
        else:
            temp_list.append('No')
    return temp_list
    # end of function


if __name__ == '__main__':
    
    # taking two inputs with space separated
    #input1 = input("Enter 1st list of words").split()
    #input2 = input("Enter 2nd list of words").split()

    input1 = 'ab bc ee fg'.split()
    input2 = 'bc fg er kl'.split()

    print(f'Provided \n\tinput1 : {input1} \n\tinput2 = {input2}')

    # calling function by passing two inputs
    result = char_trace(input1, input2)

    print(result)

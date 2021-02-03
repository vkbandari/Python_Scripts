'''
--------------------day03 : 29-01-21-------------
'''  
# generating a password Alphanumeric with symbols
import random
#print(random.randint(5,10))

# initialization of all characters in string form.
small_letters="abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols ="!@#$%^&*~`_+="
numbers= "1234567890"

# empty string to store
password = ''

'''
# if needed compulsory of 4 types, uncomment it and change loop range to 4, 10.
length = len(small_letters)
rand_index = random.randint(0,length-1)
password += small_letters[rand_index]

length = len(capital_letters)
rand_index = random.randint(0,length-1)
password += capital_letters[rand_index]

length = len(symbols)
rand_index = random.randint(0,length-1)
password += symbols[rand_index]

length = len(numbers)
rand_index = random.randint(0,length-1)
password += numbers[rand_index]

'''

# excepting 10 characters in password
for i in range(0,10):
    
	# generating random value to consider character type
    rand = random.randint(0,3)
    #print(rand)
    
	if rand == 0:
        # perform on small letters
        length = len(small_letters)
        rand_index = random.randint(0,length-1)
        password += small_letters[rand_index]
    
	elif rand == 1:
        # performing on capital letters
        length = len(capital_letters)
        rand_index = random.randint(0,length-1)
        password += capital_letters[rand_index]
    
	elif rand == 2:
        # performing on symbols
        length = len(symbols)
        rand_index = random.randint(0,length-1)
        password += symbols[rand_index]        
    
	else:
        # considering numbers
        length = len(numbers)
        rand_index = random.randint(0,length-1)
        password += numbers[rand_index]

 
print('password generated is : ', password)
 
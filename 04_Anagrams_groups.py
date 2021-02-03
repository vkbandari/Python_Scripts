'''
--------------------day04 : 02-02-21-------------
'''
# find anagrams groups and return its length----------------------------------

def anagrams(w, li_dic):
        '''
	  * Here at each iteration, the particular repeated dictionary of characters checks with other dictionaries in list of dictionary.
	  * i and j are index postions of dictionaries in list.
	  * if i and j are equal then we are on same word and if i and j th dictionaries of same length then process the operation.
	  * then check each ith dict character's occurences in jth dict characters occurences, if fails skip it, at end else append that it in result list that dictionary.
	  :return: result list contains dictionary
        '''
        result_dic = []
        for i in range(len(li_dic)):
                for j in range(len(li_dic)):
                        if i != j and len(li_dic[i]) == len(li_dic[j]):
                                #print(li_dic[i])
                                for k in li_dic[i].keys():
                                        if li_dic[i].get(k) != li_dic[j].get(k,0):
                                                break
                                else:
                                        result_dic.append([li_dic[i], li_dic[j]])
        return result_dic
	# end of function
	
if __name__ == '__main__':
        # array of words
        words = ['cat', 'listen', 'silent', 'kitten', 'salient', 'tac', 'cold', 'amb', 'frog', 'mba']
        
		# input
        # words = input("Enter words with space separated : ").split()
        print(words)
        
		# list of dictionary
        list_dic = []
        
		# finding number of times each character repeats in each word
        for word in words:
                temp_d = {}
                for char in word:
                        temp_d[char] = temp_d.get(char,0)+1
                list_dic.append(temp_d)
		
		# function call.
        result = anagrams(words, list_dic)
        
		# print the resultant groups count...
        print(len(words)-len(result)//2)

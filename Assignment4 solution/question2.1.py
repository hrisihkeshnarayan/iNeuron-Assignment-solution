2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.


## Solution

def words_into_number(lst):
    long_words = [ ]
    for name in lst:
        
        long_words.append(len(name))
            
    return long_words


words_into_number(['name','hrishikesh','tushar','ayush','ankit','avinash'])

## OUTPUT

[4, 10, 6, 5, 5, 7]

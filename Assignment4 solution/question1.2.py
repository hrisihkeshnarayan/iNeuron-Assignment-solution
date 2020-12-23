##1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
##the list of words that are longer than n.

## CODE

def filter_long_words(ls,n):
    long_words = [ ]
    for name in ls:
        if len(name) > n:
            long_words.append(name)
            
    return long_words


filter_long_words(['name','hrishikesh','tushar','ayush','ankit','avinash'],5)

##OUTPUT

['hrishikesh', 'tushar', 'avinash']
​

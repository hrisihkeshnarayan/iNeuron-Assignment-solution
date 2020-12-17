## Problem_1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

#Solution

#Sum of First n Natural numbers , Ask user for Number.


def myreduce(num):
    ''' This functionm will return sum of n Natural numbers'''
    num_list=list(range(1,number+1))
    sum_of_elements=0
    
    for i in num_list:
        sum_of_elements+=i
        
    return num_list,sum_of_elements

#Input 
print("Input:")
number=int(input("Please insert the number :"))

#Function Execution

output_value=myreduce(number)

#Output
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])

Input:
Please insert the number :20
Output:
List of First n Natural numbers are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Sum of List elements are : 210


## 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()


# Solution

# Filter the even and odd number from list which are multiples  of 5

#Input 

print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))


def myfilter(num_list):
    '''This function will filter even and odd numbers from list which are multiples of 5 '''
    num_even_list=[]
    num_odd_list=[]
    
    for i in num_list:
        if(i%5==0):
            if(i%2==0):
                num_even_list.append(i)
            else:
                num_odd_list.append(i)
                
    return num_even_list,num_odd_list


#Function Execution
output_value=myfilter(num_list)

#Output

print("Output:")
print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",output_value[0])
print("List of Odd numbers, which are multiples of 5 are:",output_value[1])



Input:
Please insert the number: 25
Output:
List of numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
List of Even numbers, which are multiples of 5 are: [10, 20]
List of Odd numbers, which are multiples of 5 are: [5, 15, 25]

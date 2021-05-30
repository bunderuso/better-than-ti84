#custom imports
from math_operations.math_time import math_main
#defining the parser function
def parser(expression):

    #calling in the input parser
    parsed_input = input_parser(expression)

    #test print statement
    print(parsed_input)

    #doing the math on the input parser
    answer = math_main(parsed_input)


#defining the input parser
def input_parser(expression):
    #defining comparison variables
    numbers = "1234567890"
    parsed_exp = []

    #going through the expression
    i = 0
    while i  < len(expression):
        #checking if we found a number
        if expression[i] in numbers:
            #defining while loop counter
            start = 0
            start = len(expression) - i
            start = len(expression) - start

            #number storing string
            num_store = ''

            #defining while loop
            while start < len(expression):
                #adding the numbers to the storage 
                if expression[start] in numbers:
                    num_store = num_store + expression[start]
                    start = start + 1
                else: 
                    break
            
            #adding the number to the expression list
            parsed_exp.append(num_store)

            #adjusting the i varaible 
            i = start + i
        
        #checking if we found a +
        elif expression[i] == '+':
            parsed_exp.append('+')
        
        #checking if we found a -
        elif expression[i] == '-':
            parsed_exp.append('-')

        #iterating the i value
        i = i + 1
    return parsed_exp

parser("1234 + 567890")
#custom imports
from math_operations.math_time import math_main
from parse_functs.parenthesis import paren_parser
#defining the parser function
def parser(expression):

    #calling in the input parser
    parsed_input, operations = input_parser(expression)

    #test print statement
    print(parsed_input)

    #doing the math on the input parser
    answer = math_main(parsed_input, operations)

    #returning the result
    return answer


#defining the input parser
def input_parser(expression):
    print("Inputted: ", expression)
    #defining comparison variables
    numbers = "1234567890~"
    parens = "()"
    parsed_exp = []
    operations = {
        "parenthesis": 0,
        "exponents" : 0,
        "multiplication" : 0,
        "division" : 0,
        "addition" : 0,
        "subtraction" : 0
    }

    #going through the expression
    i = 0
    while i  < len(expression):

        #setting the flag 
        flag = 1

        #checking if we found parenthesis
        if expression[i] in parens:
            #call the parenthesis function to parse 
            store = paren_parser(expression, i)
            
        #checking if we found a number
        elif expression[i] in numbers:
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
                    if expression[start] == "~":
                        num_store = num_store + "-"
                    else:
                        num_store = num_store + expression[start]
                    start = start + 1
                    
                else: 
                    break
            
            #adding the number to the expression list
            parsed_exp.append(num_store)

            #adjusting the i varaible 
            i = start
            flag = 0
        
        #checking if we found a +
        elif expression[i] == '+':
            parsed_exp.append('+')
            operations["addition"] = 1
        
        #checking if we found a -
        elif expression[i] == '-':
            parsed_exp.append('-')
            operations["subtraction"] = 1

        #checking if we found a *
        elif expression[i] == '*':
            parsed_exp.append('*')
            operations["multiplication"] = 1

        #checking if we found a /
        elif expression[i] == '/':
            parsed_exp.append('/')
            operations["division"] = 1

        #checking if we found a ^
        elif expression[i] == '^':
            parsed_exp.append('^')
            operations["exponents"] = 1

        #iterating the i value
        if flag == 1:
            i = i + 1
        
    return parsed_exp, operations
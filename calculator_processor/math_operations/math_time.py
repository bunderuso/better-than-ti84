import math 

def math_main(parsed_input, operations):
    #check for order of operations 
        
    #TODO check for parenthesis 
    
    #TODO check for exponents
    if operations["exponents"] == 1:
        result = exponents(parsed_input)

    #TODO check for multiplication
    if operations["multiplication"] == 1:
        result = multiplication(parsed_input)

    #TODO check for division
    if operations["division"] == 1:
        result = division(parsed_input)

    #TODO check for addition 
    if operations["addition"] == 1:
        result = addition(parsed_input)

    #TODO check for subtraction
    if operations["subtraction"] == 1:
        result = subtraction(parsed_input)

    return result

#TODO Check for parenthesis
def parenthesis(parsed_input):
    return 0

#TODO Check for exponents
def exponents(parsed_input):
    i = 0
    while i < len(parsed_input):
        if parsed_input[i] == "^":
            #getting the base and power
            base = int(parsed_input[i-1])
            power = int(parsed_input[i+1])

            #doing the exponention
            result = math.pow(base, power)
            
            #editing the input list
            parsed_input[i-1] = result
            parsed_input.pop(i+1)
            parsed_input.pop(i)

            i = 0

        else:
            i = i + 1
    return result
    return 0

#TODO Check for multiplicaton
def multiplication(parsed_input):
    i = 0
    while i < len(parsed_input):
        if parsed_input[i] == "*":
            #doing the multiplication 
            result = int(parsed_input[i-1]) * int(parsed_input[i+1])

            #editing the input list
            parsed_input[i-1] = result
            parsed_input.pop(i+1)
            parsed_input.pop(i)

            i = 0

        else:
            i = i + 1
    return result

#TODO Check for division
def division(parsed_input):
    i = 0
    while i < len(parsed_input):
        if parsed_input[i] == "/":
            #doing the division
            result = int(parsed_input[i-1]) / int(parsed_input[i+1])

            #editing the input list
            parsed_input[i-1] = result
            parsed_input.pop(i+1)
            parsed_input.pop(i)

            i = 0

        else:
            i = i + 1
    return result

#TODO Check for addition 
def addition(parsed_input):
    i = 0
    while i < len(parsed_input):
        if parsed_input[i] == "+":
            #doing the addition
            result = int(parsed_input[i-1]) + int(parsed_input[i+1])

            #editing the input list
            parsed_input[i-1] = result
            parsed_input.pop(i+1)
            parsed_input.pop(i)

            i = 0

        else:
            i = i + 1
    return result

#TODO Check for subtraction
def subtraction(parsed_input):
    i = 0
    while i < len(parsed_input):
        if parsed_input[i] == "-":
            #doing the subtraction
            result = int(parsed_input[i-1]) - int(parsed_input[i+1])

            #editing the input list
            parsed_input[i-1] = result
            parsed_input.pop(i+1)
            parsed_input.pop(i)

            i = 0

        else:
            i = i + 1
    return result
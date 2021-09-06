#custom imports
from parser import parser
import math

#declaring the while loop to keep it running
run = True
while run == True:
    #asking the user for input
    #print("=============================")
    expression = input()

    #checking if the program needs to quit
    if expression == "quit":
        run = False
    else:
        output = parser(expression)
        print("Result: ", output)
    print("=============================")
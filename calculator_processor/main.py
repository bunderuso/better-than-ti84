#custom imports
from parser import parser

#declaring the while loop to keep it running
while True:
    #askinf the user for input
    print("=============================")
    expression = input()
    output = parser(expression)
    print("=============================")
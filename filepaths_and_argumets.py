import os
import sys
import argparse

print('-----------------------------------------------------------------------------------------')
#get the name of this python file as a string
print(__file__)
#if __name__'s value is __main__, then the file is called as main file and not as module
print(__name__)
#get current working directory path as a string
print(os.getcwd())
#or
print(os.path.dirname(__file__))
#get files in a directory as an array
print(os.listdir(os.path.dirname(__file__)))

print('-----------------------------------------------------------------------------------------')
#parse through the arguments of a python file as an array
#note that unlike above os getcwd(), here sys.argv gives us the literal value that was entered when 
#running the script, rather than a full absolute filepath
print(sys.argv)
#The first element is the filename itself
print(sys.argv[0])

print('-----------------------------------------------------------------------------------------')
#There is a certain problem with sys.argv method as it does not throw any specific error 
#if the argument is not passed or argument of invalid type is passed.
# The argparse module gracefully handles the absence and presence of parameters.

# creating an ArgumentParser object
parser = argparse.ArgumentParser()
# fetching the arguments
parser.add_argument('number', help = "Enter number to triple it.", type=int)
args = parser.parse_args()
print(args.number)
# performing some operation
print(args.number * 2)
#Python by default accepts all command line arguments as string type hence the result is 55 ie. 
#the string gets repeated twice. However, we can specify the data type we are expecting

#if __name__ == '__main__':

# https://docs.python.org/3/library/argparse.html

# Importing module
import argparse

# Usage
# python main1.py -i heyfirst -a second

# Create the parser
parser = argparse.ArgumentParser(description='Description of the argparse program')

# Add an argument
parser.add_argument('-i', '--first_argument', nargs='+', required=False, help="First argument help")
parser.add_argument('-a', '--second_argument', required=False, help="Second argument help")
parser.add_argument('-s', '--third_argument', required=False, help="Third argument help")

#parser.print_help()

# Parse the argument
#parser.parse_args(['-a', '7'])
args = parser.parse_args()

"""
if args.age:
  print(args.name, 'is', args.age, 'years old.')
"""

# Print "Hello" + the user input argument
print('Hello,', args)
#print('Hello,', args.first_argument)
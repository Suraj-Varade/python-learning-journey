'''
this is a python script to be run from the terminal.

it uses the 'if __name__' constructor at the end of the script to hook into any function.
in this case, it connect to the main() function
'''

import sys

def main(args):
    print("it is a main function, and it has access to the following variables")
    for arg in args:
        print(arg)
    print(args) # ['7_working_with_scripts.py', 'hello', 'from', 'terminal']
    print(type(args)) # <class 'list'>

if __name__ == '__main__':
    main(sys.argv)


## terminal 
## python 7_working_with_scripts.py hello from terminal
## output => 
'''
it is a main function, and it has access to the following variables
7_working_with_scripts.py
hello
from
terminal
'''
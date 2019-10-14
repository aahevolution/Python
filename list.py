# python debugger
import pdb
'''
pdb allows a program to pause and give coder chance to run
and inspect the instructions throughout the code 
'''

my_list = list(map(int, input('Enter a list of integers: ').split()))

for element in my_list:
    sum = 0
    sum += element
    pdb.set_trace() # adds a break-point

print('Sum of the elements of the list is: {}'.format(sum))

'''
next(n) # execute the next line
continue(c) # skip the current break-point & continue normally
quit(q) # quit pdb abruptly
step(s) # steps into a subroutine, etc.
'''

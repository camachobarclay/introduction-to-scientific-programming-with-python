# Section 5.1

from math import exp

p0 = 100.0
h0 = 8400

h = 8848
p = p0*exp(-h/h0)
print(p)

h = input('Input the altitude (in meters):')
h = float(h)

p0 = 100.0
h0 = 8400

p = p0*exp(-h/h0)
print(p)

n = int(input('n = ?'))

for i in range(1, n+1):
    print(2*i)


import sys
print(sys.argv)
from math import exp
h = sys.argv[1]
h = float(h)

p0 = 100.0
h0 = 8400

p = p0*exp(-h/h0)
print(p)

# Section 5.2

s = '1+2'
r = eval(s)
print(r)
type(r)

r = eval('[1, 6, 7.5] + [1, 2]')
print(r)
type(r)

i1 = eval(input('operand 1: '))
i2 = eval(input('operand 2: '))
r = i1 + i2
print(f'{type(i1)} + {type(i2)} becomes {type(r)} with value {r}.')

expression = '1 + 1'    # store expression in a string
statement = 'r = 1 + 1' # store statement in a string
q = eval(expression)
exec(statement)

print(q,r)              # results are the same

somecode = """

def f(t): 
    term1 = exp(-a*t)*sin(w1*x)
    term2 = 2*sin(w2*x)
    return term1 + term2
"""
exec(somecode)  # execute the string as Python code.

formula = input('Write a formula involving x: ')
code = f"""def f(x):
    return {formula}
"""
from math import *  # make sure we have sin, cos, log, etc.
exec(code)          # turn string formula into live function

# Now the function is defined, and we can ask the 
# user for x values and evaluate f(x)

x = 0

while x is not None:
    x = eval(input('Give x (None to quit): '))
    if x is not None:
        x = float(x)
        y = f(x)
        print(f'f({x}) = {y}')

# from math import *

# import sys

# formula = sys.argv[1]
# code = f"""
# def f(x):
#   return {formula}
# """

# exec(code)
# x = float(sys.argv[2])

#def numerical_derivative(f, x, h = 1E-5):
#   return (f(x+h) - f(x-h))/(2*h)

# print(f'Numerical derivative: {numerical_derivative(f,x)}')

############# # Section 5.3

# infile = open('data.txt','r')      # open file
#for line in infile:
    # do something
# infile.close()

# infile = open('data.txt', 'r')  # open file
# mean = 0
# lines = 0
# for line in infile:
#     number = float(line)
#     mean = mean + number
#     lines += 1
# mean = mean/lines
# print(f'The mean value is {mean}')

# with open('data.txt', 'r') as infile:       # open file
#     for line in infile:
#        # do something with line

# lines = infile.readlines()
# infile.close()
# for line in lines:
    # process line

# text = infile.read()
# process the string text

s = "This is a typical string"
csvline = "Excel;sheets;often;use;semicolon;as;separator"
print(s.split())
print(csvline.split())
print(csvline.split(';'))

# months = []
# values = []
# for line infile:
#     words = line.split()    # split into words
#     months.append(words[0])
#     values.append(float(words[1]))

# def extract_data(filename):
#     infile = open(filename, 'r')
#     infile.readline()   # skip the first line
#     months = []
#     rainfall = []
#     for line in infile:
#         words = line.split()    #words[0]: month, words[1]: rainfall
#         months.append(words[0])
#         rainfall.append(float(words[1]))
#     infile.close()  
#     months = months[:-1]        # Drop the "Year" entry
#     annual_avg = rainfall[-1]   # Store the annual average
#     rainfall = rainfall[:-1]    # Redefine to contain monthly data
#     return months, rainfall, annual_avg

# months, values, avg = extract_data('rainfall.txt')

# print('The average rainfall for the months:')
# for month, value in zip(months, values):
#     print(month, value)
# print('The average rainfall for the year:', avg)

# Section 5.4

# outfile = open(filename, 'w')   # 'w' for writing

# for data in somelist:
#    outfile.write(sometext + '\n')

# outfile.close()

# with open(filename, 'w') as outfile:    # 'w' for writing
#     for data in somelist:
#         outfile.write(sometext + '\n')
data = [[ 0.75, 0.29619813, -0.29619813, -0.75 ],[ 0.29619813, 0.11697778, -0.11697778, -0.29619813], [-0.29619813, -0.11697778, 0.11697778, 0.29619813],[-0.75, -0.29619813, 0.29619813, 0.75 ]]

with open('tmp_table.dat', 'w') as outfile:
    for row in data:
        for column in row:
            outfile.write(f'{column:14.8f}')
        outfile.write('\n')

# Section 5.5

import sys
if len(sys.argv) < 3:
    print('You failed to provide a command line arg.!')
    exit()  # abort
from math import exp

h = sys.argv[1]
h = float(h)

p0 = 100.0; h0 = 8400
print(p0*exp(-h/h0))

# try:
#     <statements we intend to do>
# except:
#   <statements for handling errors>

# import sys

# try:
#   h = float(sys.argv[1])
# except IndexError:
#   print('No command line argument for h!')
#   sys.exit(1)     # abort execution
# except ValueError:
#   print(f'h must be a pure number, not {sys.argv[1]}')
#   exit()

# p0 = 100.0; h0 = 8400
# print(p0*exp(-h/h0))

# except:
#   print('Something went wrong in reading input data!')
#   exit()

# import sys
# def read_altitude():
#   try:
#       h = float(sys.argv[1])
#   except IndexError('The altitude must be supplied on command line.')
#       # re-raise, but with specific explanation:
#       raise ValueError(
#       f'Altitude must be number, not "{sys.argv[1]}".')

# h is read correctly as a number, but has a wrong value:
# if h < -430 or h > 13000:
#   raise ValueError(f'The formula is not valied for h={h}')
# return h

# try:
#   h = read_altitude()
# except (IndexError, ValueError) as e:
# print exception message and stop the program
# print(e)
# exit()

# Section 5.6

from math import log

r = log(6)      # call log function in math module

import sys
x = eval(sys.argv[1])   # access list argv in sys module

from math import log as ln

def present_amount(P, r, n):
    return P*(1+r/100)**n

def initial_amount(A,r,n):
    return A*(1+r/100)**(-n)

def years(P,A,r):
    return ln(A/P)/ln(1+r/100)

def annual_rate(P,A,n):
    return 100*((A/P)**(1.0/n) - 1)

# from interest import years
# P = 1; r = 5
# n = years(P,2*P, p)
# print(f'Money has doubled after {n} years')

# if __name__ == '__main__':  # this test defines the test block
#     <block of statements>

# if __name__ == ’__main__’:
#  A = 2.31525
#  P = 2.0
#  r = 5
#  n = 3
#  A_ = present_amount(P, r, n)
#  P_ = initial_amount(A, r, n)
#  n_ = years(P, A, r)
#  r_ = annual_rate(P, A, n)
#  print(f’A={A_} ({A}) P={P_} ({A}) n={n_} ({n}) r={r_} ({p})’)

# def test_all_functions():
#   # Define compatible values
#   A = 2.31525; P = 2.0; r = 5.0; n = 3
#   #Given three of these, compute the remaining one
#   #and compare with the correct value (in parenthesis)
#   A_computed = present_amount(P, r, n)
#   P_computed = initial_amount(A, r, n)
#   n_computed = years(P, A, r)
#   r_computed = annual_rate(P, A, n)
#   def float_eq(a, b, tolerance=1E-12):
#       """Return True if a == b within the tolerance."""
#       return abs(a - b) < tolerance
#   success = float_eq(A_computed, A) and \
#       float_eq(A0_computed, A0) and \
#       float_eq(p_computed, p) and \
#       float_eq(n_computed, n)
#   assert success # could add message here if desired

# if __name__ == ’__main__’:
#   test_all_functions()
import numpy

numpy.__file__
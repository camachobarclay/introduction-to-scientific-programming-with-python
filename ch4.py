# Section 4.1 

from math import*
from re import X
x = pi
y = sin(x)*log(x)
somelist = [1, 2, 3, 4, 5]
n = len(somelist)
for i in range(5, n, 2):
    print(i)
C = [5, 10, 40, 45]
C.append(50)

def amount(n):
    P = 100
    r = 5.0
    return P*(1+r/100)**n

year1 = 10
a1 = amount(year1)  # call
a2 = amount(5)      # call

print(a1, a2)
print(amount(6))    # call
a_list = [amount(year) for year in range(11)] # multiple calls

# Section 4.2

def amount(P,r,n):
    return P*(1+r/100.0)**n

# sample calls:
a1 = amount(100, 5.0, 10)
a2 = amount(10, r = 3.0, n = 6)
a3 = amount(r = 4, n= 2, P = 100)

P = 100
r = 5.0

def amount(n):
    return P*(1+r/100)**n

print(amount(7))

P = 100
r = 5.0

def amount(n):
    r = 4.0
    return P*(1+r/100)**n

print(amount(n = 6))
print(r)

# changing global variables

def amount(n):
    global r
    r = 4.0
    return P*(1+r/100)**n

print(amount(n = 6))
print(r)

def amount(n,r):
    r = r - 1.0
    a = P*(1+r/100)**n
    return a, r

a0, r = amount(10,7)
print(a0, r)

def yfunc(t,v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

# call:
position, velocity = yfunc(0.6,3)

pos_vel = yfunc(0.6,3)
print(pos_vel)
print(type(pos_vel))

def f(x):
    return x, x**2, x**4

s = f(2)
print(type(s),s)

def logsum(x,n):
    s = 0.0
    for i in range(1,n+1):
        s += x**i/i
    return s

print(logsum(1/2,1000))

# example use

x = 0.5
from math import log
print(logsum(x,3), logsum(x,10), -log(1-x))

from math import log

def L2(x,n):
    s = 0
    for i in range(1,n+1):
        s +=x**i/i   
    value_of_sum = s
    error = -log(1-x) - value_of_sum
    return value_of_sum, error

    # typical call:
x = 0.8; n = 10000
value, error = L2(x,n)
print(value, error)

def somefunc(obj):
    print(obj)

return_value = somefunc(3.4)

def table(x):
    print(f'x={x},-ln(1-x)={-log(1-x)}')
    for n in [1, 2, 10, 100]:
        value, error = L2(x,n)
        print(f'n={n:4d} approx: {value:7.6f}, error: {error:7.6f}')

table(0.5)

# Section 4.3

def somefunc(arg1, arg2, kwarg1=True, kwarg2 = 0):
    print(arg1, arg2, kwarg1, kwarg2)

somefunc('Hello',[1,2])                             # drop kwarg1 and krwarg2
somefunc('Hello',[1,2], 'Hi')                       # kwarg2 has default value
somefunc('Hello',[1,2], 'Hi', 6)                    # All variables assigned a value
somefunc('Hello', [1,2], kwarg2 = 'Hi')             #kward2 changed, kwarg1 has default values
somefunc('Hello', [1,2], kwarg2 = 'Hi', kwarg1 = 6) #specify all args

def yfunc(t, v0 = 5, g = 9.81):
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

# example calls:
y1, dy1 = yfunc(0.2)
y2, dy2 = yfunc(0.2, v0 = 7.5)
y3, dy3 = yfunc(0.2, 7.5, 10.0)

def amount(P, r, n):
    """Compute the growth of an investment over time."""
    a = P*(1+r/100)**n
    return a

def line(x0, y0, x1, y1):
    """
    Compute the coefficients a and b in the mathematical 
    expression for a straight line y = a*x + b that goes 
    through two points (x0, y0) and (x1, y1).
    
    x0, y0: a point on the line (floats).
    x1, y1: another point on the line (floats).
    return a, b (floats) for the line (y = a*x + b)
    """

    a = (y1 - y0)/(x1 - x0)
    b = y0 - a*x0
    return a, b

from math import sin, pi

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0
print(f(0.5))
print(f(5*pi))

#   if condition:
#       <block of statements, executed if condition is True>
#
# <next line after if-block, always executed>

#   if condition:
#       <block of statements, executed if condition is True>
#   else:
#       <block of statements, executed if condition is False>

#   if condition1:
#       <block of statements>
#   elif condition2:
#       <block of statements>
#   elif condition3:
#        <block of statements>
#   else:
#       <block of statements>
#   <next statement>

# The piecewise function N(x) =
# 0, if x < 0
# x, if 0 <= x < 1
# 2 - x, 1 <= x < 2
# 0, x => 2

def N(x):
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2 - x
    elif x >= 2:
        return 0


#   if condition:
#       variable = value1
#   else:
#       variable = value2

#can be rewritten as

#   variable = (value if condition else value2)

def f(x):
    return (sin(x) if 0 <= x <= pi else 0)

# Section 4.5

def diff2(f, x, h = 1E-6):
    r = (f(x-h) - 2*f(x) + f(x+h))/float(h**2)
    return r

def f(x):
    return x**2 - 1

df2 = diff2(f,1.5)
print(df2)

f = lambda x: x**2 - 1 # a lambda function

# Lambda function formulation:
#   somefunc = lambda a1, a2, ...: some_expression 
# is equivalent to
#   def somefunc(a1, a2, ...):
#       return some_expression

df2 = diff2(lambda x: x**2 - 1, 1.5)
print(df2)

# Section 4.6

from math import exp

def bisection(f, a, b, tol = 1e-3):
    if f(a)*f(b) > 0:
        print(f'No roots or more than one root in [{a},{b}')
        return

    m = (a+b)/2

    while abs(f(m)) > tol:
        if f(a)*f(m) <0:
            b = m
        else:
            a = m
        m = (a+b)/2
    
    return m

# call the method for f(x) = = x**2 - 4*x + exp(-x)
f = lambda x: x**2 - 4*x +exp(-x)
sol = bisection(f, -0.5, 1, 1e-6)

print(f'x = {sol:g} is an approximate root, f({sol:g}) = {f(sol):g}')

from math import expm1

def Newton(f, dfdx, x0, max_it = 200, tol= 1e-3):
    f0 = f(x0)
    iter = 0
    while abs(f0) > tol and iter < max_it:
        x1 = x0 - f0/dfdx(x0)
        x0 = x1
        f0 = f(x0)
        iter += 1
    
    converged = iter < max_it
    return x0, converged, iter

# call the method for f(x) = x**2 - 4*x + exp(-x)

f = lambda x: x**2 - 4*x + exp(-x)
dfdx = lambda x: 2*x - 4 - exp(-x)

sol, converged, iter = Newton(f, dfdx, 0, 1e-6)

if converged:
    print(f'x = {sol:g} is an approximate root, f({sol:g}) = {f(sol):g}')
else:
    print(f'The method did not converge')

def double(x):      # some function
    return 2*x

def test_double():      # associated test functino
    x = 4               # some chosen x value
    expected = 8        # expected results from double(x)
    computed = double(x)
    success = computed == expected  # Boolean value: test passed?
    msg = f'computed {computed}, expected {expected}'
    assert success, msg

from math import sin, pi

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0

def test_f():
    x1, exp1 = -1.0, 0.0
    x2, exp2 = pi/2, 1.0
    x3, exp3 = 3.5, 0.0

    tol = 1e-10
    assert abs(f(x1) - exp1) < tol, f'Failed for x = {x1}'
    assert abs(f(x2) - exp2) < tol, f'Failed for x = {x2}'
    assert abs(f(x3) - exp3) < tol, f'Failed for x = {x3}'

from math import sin, pi

def f(x):
    if 0 <= x <= pi:
        return sin(x)
    else:
        return 0

def test_f():
    x_vals = [-1, pi/2, 3.5]
    exp_vals = [0.0, 1.0, 0.0]
    tol = 1e-10
    for x, exp in zip(x_vals, exp_vals):
        assert abs(f(x) - exp) < tol, \
            f'Failed for x = {x}, expected {exp}, but got {f(x)}'
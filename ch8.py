from math import *
from numpy import *

def barometric(h,T):
    g = 9.81    # m/(s*s)
    R = 8.314   # J/(K*mol)
    M = 0.02896 # kg/mol
    p0 = 100.0  #kPa

    return p0*exp(-M*g*h/(R*T))

T = 245.0

def barometric(h):
    g = 9.81    # m/(s*s)
    R = 8.314   # J/(K*mol)
    M = 0.02896 # kg/mol
    p0 = 100.0  #kPa

    return p0*exp(-M*g*h/(R*T))

class Barometric:
    def __init__(self,T):
        self.T = T          # K
        self.g = 9.81       # m/(s*s)
        self.R = 8.314      # J(K*mol)
        self.M = 0.02896    # kg/mol
        self.p0 = 100.0     # kPA
    
    def value(self, h):
        return self.p0 * exp(-self.M*self.g*h/(self.R*self.T))

b1 = Barometric(T = 245)        # create instance (object)
p1 = b1.value(2469)             # compute function value
b2 = Barometric(T = 273)
p2 = b2.value(2469)

print(b1)
print(b2)

class Barometric1:
    def __init__(self,T):
        self.T = T

    def value(self,h):
        g = 9.81
        R = 9.314
        M = 0.02896 
        p0 = 100.0
        return p0*exp(-M*g*h/(R*self.T))

class Barometric2:
    def __init__(self,T):
        g = 9.81        # m/(s*s)
        R = 8.314       # J/(K*mol)
        M = 0.02896     # kg/mol
        self.h0 = R*T/(M*g)
        self.p0 = 100.0     #kPA

    def value(self, h):
        return self.p0*exp(-h/self.h0)

# p1 = b1.value(2469)

# is equivalent to

# p1 = Barometric.value(b1, 2469)

from math import sin, exp, pi

def make_table(f, tstop, n):
    for t in linspace(0, tstop, n):
        print(t, f(t))

def g(t):
    return sin(t)*exp(-t)

make_table(g, 2*pi, 11)     # send ordinary function

b1 = Barometric(2469)
make_table(b1.value, 2*pi, 11)  # send class method

# class MyClass:
#     def __init__(self, p1, p2,...):
#         self.attr1 = p1
#         self.attr2 = p2
#     ...
#
#     def method1(self, arg):
#         # access attributes with self prefix
#         result = self.attr1 + ...
#         ...
#         # create new attributes if desired
#         self.attrx = arg
#         ...
#         return result
#
#     def method2(self):
#         ...
#         print(...)

# m = MyClass(p1, p2)
# m.new_attr = p3

# Section 8.2

class Account:
    def __init__(self,first_name, last_name, number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def print_info(self):
        first = self.first_name
        last = self.last_name
        number = self.number
        bal = self.balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)
    

a1 = Account('John', 'Olsson', 19371554951, 20000)
a2 = Account('Liz', 'Olsson', 19371564761, 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print("a1's balance:", a1.balance)
a1.print_info()
a2.print_info()

a1.first_name = 'Some other name'
a1.balance = 1000000
a1.number = '193715647688'

class AccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount
    
    def get_balance(self):      # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self.first_name; last = self._last_name
        number = self.number; bal = self.balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)

a1 = AccountP('John', 'Olsson', '19371554951', 20000)
a1._number = '19371554955'

# Section 8.3

class Barometric:
    def __init__(self,T):
        self.T = T          # K
        self.g = 9.81       # m/(s*s)
        self.R = 8.314      # J/(k*mol)
        self.M = 0.0896     # kg/mol
        self.p0 = 100.0     # kPA

    def __call__(self,h):
        return self.p0*exp(-self.M*self.g*h/(self.R*self.T))

    def __str__(self):
        return f'p0*exp(-M*g*h/(R*T)); T = {self.T}'

    def __add__(self, otherBarometric):
        return(self.T + otherBarometric.T)

    def __repr__(self):
        ###Return code for regenerating this instance.###
        return f'Barometric({self.T})'

baro = Barometric(245)
p = baro(2346)      #same a p = baro.__call__(2346)
b = Barometric(245)
print(b(2469))
print(b)


# c = a + b     # c = a.__add__(b)
# c = a - b     # c = a.__sub__(b)
# c = a*b       # c = a.__mul__(b)
# c = a/b       # c = a.__div__(b)
# c = a***e     # c = a.__pow__(e)

# a == b        # a.__eq__(b) 
# a != b        # a.__ne__(b)
# a < b         # a.__lt__(b)
# a <= b        # a.__le__(b)
# a > b         # a.__gt__(b)
# a >= b        # a.__ge__(b)

from tmp import *

b = Barometric(271)
print(b)
repr(b)
b2 = eval(repr(b))
print(b2)

class A:
    """A class for demo purposes."""
    def __init__(self,value):
        self.v = value

a = A(2)

print(dir(a))
print(a.__doc__)
print(a.__dict__)
print(a.v)
print(a.__module__)


a = A([1,2])
print(a.__dict__)   # all attributes

a.myvar = 10        # add new attribute (!)

print(a.__dict__)

# Section 8.4

def f(x):
    return x**3

# want dfdx = Derivative(f) so that print(dfdx(2))  # computes 3*x**2 for x = 2

class Derivative:
    def __init__(self, f, h = 1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self,x):
        f, h = self.f, self.h   # make short forms
        return (f(x+h) - f(x))/h

from math import *
df = Derivative(sin)
x = pi
print(df(x))
print(cos(x))

dg = Derivative(f)
t = 1
print(dg(t))    # compare with 3 (exact)

def Newton2(f, dfdx, x0, max_it=20, tol= 1e-3):

    f0 = f(x0)
    iter = 0

    while abs(f0) > tol and iter < max_it:
        x1 = x0 - f0/dfdx(x0)
        x0 = x1
        f0 = f(x0)
        iter += 1

    converged = iter < max_it
    return x0, converged, iter

def g(x):
    return 100000*(x-0.9)**2*(x-1.1)**3

dgdx = Derivative(g)
xstart = 1.01
print(Newton2(g,dgdx, xstart))

# Section 8.5

def test_Derivative():
    # The formula is exact for linear functions, regardless of h
    a = 3.5; b = 8
    f = lambda x: a*x + b
    dfdx = Derivative(f, h=0.5)
    diff = abs(dfdx(4.5) - a)
    assert diff < 1E-14, 'bug in class Derivative, diff =%s' % diff

test_Derivative()

# Section 8.6

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __call__(self,x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        # return self + other

        # start with the longest list and add in the other:
        if len(self.coeff) > len(other.coeff):
            coeffsum = self.coeff[:] #copy!
            for i in range(len(other.coeff)):
                coeffsum[i] += other.coeff[i]
        else:
            coeffsum = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                coeffsum[i] += self.coeff[i]
        return Polynomial(coeffsum)

    def __mul__(self, other):
        M = len(self.coeff) - 1
        N = len(other.coeff) - 1
        coeff = [0]*(M+N+1) # or zeros(M+N+1)
        for i in range(0, M+1):
            for j in range(0,N+1):
                coeff[i+j] += self.coeff[i]*other.coeff[j]
        return Polynomial(coeff)
    
    def differentiate(self):    # change self
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]
    
    def derivative(self):   # return new polynomial
        dpdx = Polynomial(self.coeff[:])    # copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s =  ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += f' + {self.coeff[i]:g}*x^{i:g}'
            # fix layout (many special cases):
            s = s.replace('+ -', '- ')
            s = s.replace(' 1*', ' ')
            s = s.replace('x^0', '1')
            s = s.replace('x^1 ', 'x ')
            if s[0:3] == ' + ': # remove initial +
                s = '-' +s[3:]
            if s[0:3] == ' - ': # fix spaces for initial -
                s = '-' + s[3:]
            return s

p1 = Polynomial([1, -1])
print(p1)
p2 = Polynomial([0, 1, 0, 0, -6, -1])
p3 = p1 + p2
print(p3.coeff)
print(p3)
print(p3(2.0))
p4 = p1*p2
p2.differentiate()
print(p2)
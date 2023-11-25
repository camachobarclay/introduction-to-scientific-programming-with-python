# Section 9.1

import numpy as np
from math import *

class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1
    
    def __call__(self,x):
        return self.c0 + self.c1*x
    
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in np.linspace(L, R, n):
            y = self(x)
            s += f'{x:12g} {y:12g}\n'
        return s

class parabola:
    def __init(self,c0,c1,c2):
        self.c0, self.c1, self.c2 = c0, c1, c2
    
    def __call__(self,x):
        return self.c2*x**2 + self.c1*x + self.c0
    
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in linspace(L,R,n):
            y = self(x)
            s += f'{x:12g} {y:12g}\n'
        return s

# class Parabola(Line):
#     pass  # for when the compiler is expecting code

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        super().__init__(c0,c1) # Lines
        self.c2 = c2
    def __call__(self,x):
        return super().__call__(x) + self.c2*x**2

# SuperClassName.method(self, arg1, arg2,...)
# super().method(arg1, arg2,...)

p = Parabola(1, -2, 2)
p1 = p(2.5)
print(p1)
print(p.table(0, 1, 3))
l = Line(-1,1)
print(isinstance(l, Line))
print(isinstance(l, Parabola))
p = Parabola(-1, 0 , 10)
print(isinstance(p, Parabola))
print(isinstance(p, Line))
print(issubclass(Parabola,Line))
print(issubclass(Line,Parabola))
print(p.__class__ == Parabola)
print(p.__class__.__name__)

class PARABOLA:
    def __init__(self, c0, c1, c2):
        self.c0, self.c2 = c0, c1, c2

    def __call__(self,x):
        return self.c2*x**2 + self.c1*x + self.c0

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        for x in linspace(L,R,n):
            y = self(x)
            s += '%12g %12g\n' % (x,y)
        return s

class LINE(PARABOLA):
    def __init__(self, c0, c1):
        super().__init__(c0,c1,0)

# Section 9.2

class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self,x):
        f, h = self.f, self.h   # make shortt forms
        return (f(x+h) - f(x))/h


def f(x):
    return exp(-x)*sin(4*pi*x)

dfdx = Derivative(f)
print(dfdx(1.2))

class Forward:
    def __init__(self, f, h = 1E-5):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Central2:
    def __init__(self, f, h = 1E-5):
        self.f, self.h = f, h

    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Central4:
    def __init__(self, f, h= 1E-5):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h) - f(x - h))/(2*h) - (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)

class Diff:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h

class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x - h))/(2*h)

class Central4(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h) - f(x-h))/(2*h) - (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)

mycos = Central4(sin)
print(mycos(pi))

h = [1.0/(2**i) for i in range(5)]
ref = cos(pi/4)

print(f'    h    Forward1    Central2    Central4')
for h_ in h:
    f1 = Forward1(sin,h_); c2 = Central2(sin,h_); c4 = Central4(sin,h_)
    e1 = abs(f1(pi/4) - ref)
    e2 = abs(c2(pi/4) - ref)
    e4 = abs(c4(pi/4) - ref)
    print(f'{h_:1.8f}  {e1:1.10f}. {e2:>1.10f}  {e4:>1.10f}')

# Section 9.3

class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in clas %s' % \
            self.__class__.__name__)

    def integrate(self,f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

    def vectorized_integrate(self,f):
        # f must be vectorized for this to work
        return dot(self.weights, f(self.points))

class Trapezoidal(Integrator):
    def construct_method(self):
        h = (self.b - self.a)/float(self.n - 1)
        x = np.linspace(self.a, self.b, self.n)
        w = np.zeros(len(x))
        w[1:-1] += h
        w[0] = h/2;   w[-1] = h/2
        return x,w

class Midpoint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n    # quick forms
        h = (b-a)/float(n)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
        return x, w

class Simpson(Integrator):
    def construct_method(self):
        if self.n % 2!=1:
            print('n = %d must be odd, 1 is added %d', self.n)
            self.n += 1
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)*2
        w = np.zeros(len(x))
        w[0:self.n:2] = h*1.0/3
        w[1:self.n:2] = h*2.0/3
        w[0] /= 2
        w[-1] /= 2
        return x, w

def f(x):
    return x*x

trapez = Trapezoidal(0,2,101)
print(f'Trapezoidal rule = {trapez.integrate(f)}')
mp = Midpoint(0,2,101)
print(f'Midpoint Rules = {mp.integrate(f)}')
simpson = Simpson(0,2,101)
print(f'Simpsons Rules = {simpson.integrate(f)}')
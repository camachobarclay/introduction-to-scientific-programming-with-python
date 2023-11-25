#import sys
#sys.path.append("c:\users\frank camacho\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (1.4)")

# Section 6.1 

def f(x):
    return x**2

n = 5               # number of points
dx = 1.0/(n-1)      # x spacing in [0,1]
print(f'n = {n}, dx = {dx}')


xlist = [i*dx for i in range(n)]
ylist = [f(x) for x in xlist]

print(f'xlist = {xlist}')
print(f'ylist = {ylist}')

import numpy as np      # module for arrays

x = np.array(xlist)     # turn list xlist into array
y = np.array(ylist)

print(f'x = {x}')
print(f'y = {y}')

x = np.linspace(0,1,n) # n points in [0,1]
y = np.zeros(n)        # n zeros (float data type)

print(f'x = {x}')
print(f'y = {y}')

for i in range(n):
    y[i] = f(x[i])

print(f'y = {y}')

from math import cos
x = np.linspace(0,1,11)
y = np.zeros(len(x))

print(f'x = {x}')
print(f'y = {y}')

for i in range(len(x)):
    y[i] = cos(x[i])

y = np.cos(x)       # x: array, y: array

print(f'y = {y}')

from numpy import sin, exp, linspace

def g(x):
    return x**2 + 2*x -4

def f(x):
    return sin(x)*exp(-2*x)

x = 1.2                     # float object
y = f(x)                    # y is a float

print(f'x = {x}')
print(f'y = {y}')


x = linspace(0,3,101)       # 100 intervals in [0,3]
y = f(x)                    # y is array
z = g(x)                    # z is array>>> import math, numpy

print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

# >>> x = numpy.linspace(0, 1, 6)
# >>> x
# array([0. , 0.2, 0.4, 0.6, 0.8, 1. ])
# >>> math.cos(x[0])
# 1.0
# >>> math.cos(x)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: only size-1 arrays can be converted to Python scalars
# >>> numpy.cos(x)
# array([1. , 0.98006658, 0.92106099, 0.82533561, 0.69670671,
# 0.54030231])


n = 100
x = np.linspace(0,4,n+1)
y = np.exp(-x)*np.sin(2*np.pi*x)

print(f'x = {x}')
print(f'y = {y}')

# Section 6.2

import matplotlib.pyplot as plt

n = 100
x = np.linspace(0,4,n+1)
y = np.exp(-x)*np.sin(2*np.pi*x)

print(f'x = {x}')
print(f'y = {y}')

plt.plot(x,y)
plt.show()

def f(x):
    return np.exp(-x)*np.sin(2*np.pi*x)

n = 100
x = np.linspace(0,4,n+1)
y = f(x)

plt.plot(x,y, label = 'exp(-x)*sin(2$\pi$)')
plt.xlabel('x')             # label on the x axis
plt.ylabel('y')             # label on the y axis
plt.legend()                # mark the curve
plt.axis([0, 4, -0.5, 0.8]) # [tmin, tmax, ymin, ymax]

plt.title('My First Matplotlib Demo')

plt.savefig('fig.pdf')      # make PDF image for reports
plt.savefig('fig.png')      # make PNG image for web pages
plt.show()

def f1(x):
    return np.exp(-x)*np.sin(2*np.pi*x)

def f2(x):
    return np.exp(-2*x)*np.sin(4*np.pi*x)

x = np.linspace(0,8,401)

y1 = f1(x)
y2 = f2(x)

plt.plot(x,y1,'r--', label = 'exp(-x)*sin(2$\pi$ x)')
plt.plot(x,y2, 'g:', label = 'exp(-2*x)*sin(4$\pi$ x)')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Plotting two curves in the same plot')
plt.savefig('fig_two_curves.png')
plt.show()

t = np.linspace(0,8,201)
plt.plot(x,np.exp(-x)*np.sin(2*np.pi*x), x,np.exp(-2*x)*np.sin(4*np.pi*x))
plt.show()

from numpy import *
import matplotlib.pyplot as plt

formula = input('Write a mathematical expressio of x:')
xmin = float(input('Provide lower bound for x:'))
xmax = float(input('Provide upper bound for x:'))

x = linspace(xmin, xmax, 101)
y = eval(formula)

plt.plot(x,y)
plt.show()

# Section 6.3

def H(x):
    if x < 0:
        return 0
    else:
        return 1

# x = linspace(-10, 10, 5)
# y = H(x)
# plot(x, y)

# >>> x = linspace(-10,10,5)
# >>> x
# array([-10., -5., 0., 5., 10.])
# >>> b = x < 0
# >>> b
# array([ True, True, False, False, False], dtype=bool)
# >>> bool(b) # evaluate b in a Boolean context
# ...
# ValueError: The truth value of an array with more than
# one element is ambiguous. Use a.any() or a.all()

import numpy as np
import matplotlib.pyplot as plt

n = 5
x = np.linspace(-5,5,n+1)
y = np.zeros(n+1)

for i in range(len(x)):
    y[i] = H(x[i])

plt.plot(x,y)
plt.show()

def H_loop(x):
    r = np.zeros(len(x))    # or r = x.copy()
    for i in range(len(x)):
        r[i] = H(x[i])
    return r

n = 5
x = np.linspace(-5,5,n+1)
y = H_loop(x)

Hv = np.vectorize(H)

def Hv(x):
    return np.where(x< 0, 0.0, 1.0)

# def f(x):
# 
#   if condition:
#       x = <expression1>
#   else:
#       x = <expression2>
#   return x
#
#   def f_vectorized(x):
#       x1 = <expression1>
#       x2 = <expression2>
#       r = np.where(condition, x1, x2)
#       return r

# Section 6.4

def f(x,m,s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0; s_start = 2; s_stop = 0.2
s_values = np.linspace(s_start, s_stop, 30)

x = np.linspace(m -3*s_start, m + 3*s_start, 1000)

# f is max for x = m (smaller s gives larger max values)

max_f = f(m, m , s_stop)

y = f(x,m,s_stop)

lines = plt.plot(x,y)   # Returns a list of line objects!

plt.axis([x[0], x[-1], -0.1, max_f])
plt.xlabel('x')
plt.ylabel('f')

for s in s_values:
    y = f(x,m,s_stop)
    lines[0].set_ydata(y) #update plot data and redraw
    plt.draw()
    plt.pause(0.1)

import matplotlib.pyplot as plt
import numpy as np

def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0; s_start = 2; s_stop = 0.2
s_values = np.linspace(s_start, s_stop, 30)

x = np.linspace(m -3*s_start, m + 3*s_start, 1000)
# f is max for x=m (smaller s gives larger max value)
max_f = f(m, m, s_stop)

y = f(x,m,s_stop)
lines = plt.plot(x,y)

plt.axis([x[0], x[-1], -0.1, max_f])
plt.xlabel('x')
plt.ylabel('f')

frame_counter = 0

for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y) #update plot data and redraw
    plt.draw()
    plt.savefig(f'tmp_{frame_counter:04d}.png') #unique filename
    frame_counter += 1

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0; s_start = 2; s_stop = 0.2
s_values = np.linspace(s_start,s_stop,30)

x = np.linspace(-3*s_start,3*s_start, 1000)

max_f = f(m,m,s_stop)

plt.axis([x[0],x[-1],0,max_f])
plt.xlabel('x')
plt.ylabel('y')

y = f(x,m,s_start)
lines = plt.plot(x,y) #initial plot to create the linespip  object

def next_frame(s):
    y = f(x, m, s)
    lines[0].set_ydata(y)
    return lines

ani = FuncAnimation(plt.gcf(), next_frame, frames=s_values, interval=100)
#ani.save('movie.mpeg',fps=20)
plt.show()

# Section 6.5

import numpy as np
x = np.linspace(0,10,101)

a = zeros(x.shape, x.dtype)
a = x.copy()

a = np.zeros_like(x) # zeros and same size as x

a = asarray(a)

a = linspace(1,8,8)
print(a)
a[[1,6,7]] = 10
print(a)
a[range(2,8,3)] = -2
print(a)
print(a<0)
print(a[a<0])
a[a<0] = a.max()
print(a)

A = zeros((4,4))
A[0,0] = -1
A[1,0] = 1
A[2,0] = 10
A[0,1] = -5
A[2,3] = -100
A[3][3] = 17

print(A)
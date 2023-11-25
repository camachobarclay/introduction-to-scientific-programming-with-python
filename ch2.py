# Section 2.1
print(100*(1+5.0/100)**7)

# Section 2.2
# program for computing the growth of money deposited in a bank

primary = 100   # initial amount
r = 5.0         # interest rate in %
n = 7           # the number of years
amount = primary*(1 + r/100)**n

# is equivalent to 
# primary = 100; r = 5.0; n = 7; amount = priimary*(1+r/100)**n

initial_amount = 100
interest_rate = 5.0
number_of_years = 7
final_amount = initial_amount*(1 + interest_rate/100)**number_of_years
print(final_amount)

t = 0.6
t = t + 0.1
print(t)

a = 5
print(a == 5)

# understanding types
hello = "Hello, World!"
print(hello)

print(type(hello))
print(type(r))
print(type(primary))
print(type(n))

print(hello + hello)
print(hello*5)

x1 = 2
x2 = "2"
print(x1+x1)
print(x2+x2)

x1 = float(x1)
x2 = float(x2)
print(type(x1))
print(type(x2))
print(x1+x2)

# Section 2.3

print(primary, final_amount)
print(f"After {n} years, 100 EUR has grown to {amount} EUR.")

print(f"2+2 = {2+2}")

t = 1.234567
print(f"Default output gives t = {t}.")
print(f"We can set the precision: t = {t:.2}.")
print(f"Or control the number of decimals: t = {t:.2f}")

print(f"We may set the space used for the output: t = {t:8.2f}.")

r = 87
print(f"Integer set to occupy exactly 8 chars of space: r = {r:8d}")

a = 786345687.12
b = 1.2345

print(f"Without the format specifier: a = {a}, b = {b}.")
print(f"With the format specifier: a = {a:g}, b = {b:g}.")

# Section 2.4

import math
r = math.sqrt(2)
# or 
from math import sqrt
r = sqrt(2)
# or
from math import* #import everything in math
r = sqrt(2);

from math import pi, exp

m = 0
s = 2
x = 1.0
f = 1/(sqrt(2*pi)*s)*exp(-0.5*((x-m)/2)**2)
print(f)

print(dir(math))

# Section 2.5
v1 = 1/49.0*49
v2 = 1/51.0*51
print(f"{v1:.16f} {v2:.16f}")

print(v1 == 1)
print(v2 == 1)

tol = 1e-14
print(abs(v1-1)<tol)
print(abs(v2-1)<tol)

print(5.0/100)
print(5/100)
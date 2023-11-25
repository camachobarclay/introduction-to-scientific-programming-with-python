# Section 3.1
# Recall previous example

from tkinter import N
from webbrowser import GenericBrowser


P = 100
r = 5.0
n = 7
A = P*(1+r/100)**n 
print(n,A)

# Bad way to do the loop, but it works:
# P =100; r = 5.0;
# n=0; A = P * (1+r/100)**n; print(n,A)
# n=1; A = P * (1+r/100)**n; print(n,A)
# ...
# n=9; A = P * (1+r/100)**n; print(n,A)
# n=10; A = P * (1+r/100)**n; print(n,A)

# syntax of while condition loop is
# while condition:
#   <statement 1>
#   <statement 2>
#   ...
#   <first statement after the loop>

P = 100
r = 5.0
n = 0

while n <= 10:              # loop heading with condition
    A = P*(1+r/100)**n      # 1st statement inside loop
    print(n,A)              # 2nd statement inside loop
    n = n + 1               # last statement inside loop

# Section 3.2

# Bools

t = 40

print(t == 40) # note the double ==, t = 40 is an assignment
print(t != 40)
print(t >= 40)
print(t <= 40)
print(t < 40)
print(t > 40)

x = 0; y = 1.2;
print(x >= 0 and y < 1)
print(x >= 0 and y < 1)
print(x > 0 or y > 1)
print(x > 0 or not y > 1)
print(-1 < x <=0)   # same as -1 < x and x <= 0
print(not (x > 0 or y > 0))

# Section 3.3

# Don't do n0 = 0, n1 = 1,..., n10 = 10 to store a sequence of numbers, instead use a list

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L1 = [-91, 'a string', 7.2, 0]   #arbitrary list of items

print(L1[3])

mylist = [4, 6, -3.5]
print(mylist[0])
print(mylist[1])
print(mylist[2])
len(mylist)     # length of list

n.append(9) #add new element at 9 at the end
print(n)
n = n + [10,11] # extend n at the end
print(n)
print(9 in n)
del n[0]

# l[0] = 2
a = [1,2,3,4]
b = a
b[-1] = 6
a

c = a.copy()

# Section 3.4

# For loop syntax
# for element in list;
#   <statement 1>
#   <statement 2>
#   ...
# <first statement after loop>

years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = 5.0
p = 100.0
for n in years:
    A = P*(1+r/100)**n
    print(f'{n:5d}{A:8.2f}')

# Can always translate for loops to while loops--
#   for element in somelist:
#       # process element
# is equivalent to
#   index = 0
#   while index < len(somelist):
#       element = somelist[index]
#       # process element
#       index += 1

P = 100
r = 5.0
N = 10
for n in range(N+1):
    A = P*(1+r/100)**n
    print(n,A)

print(list(range(0,N+1,3)))

amounts = []

for n in range(N+1):
    A = P*(1+r/100)**n
    amounts.append(A)
print(amounts)

N = 14
S = 0
for i in range(1,N+1):
    S += i**2

v = [-1, 1, 10]
for e in v:
    e = e + 2
print(v)

v = [-1, 1, 10]

for i in range(len(v)):
    v[i] = v[i] + 2
print(v)

P = 100
r_low = 2.5
r_high = 5.0
N = 10
A_high = []
A_low = []
for n in range(N+1):
    A_low.append(P*(1+r_low/100)**n)
    A_high.append(P*(1+r_high/100)**n)

A_low = [P*(1+r_low/100)**n for n in range(N+1)]
A_high = [P*(1+r_high/100)**n for n in range(N+1)]

# newlist = [expression for element in somelist]

for i in range(len(A_low)):
    print(A_low[i], A_high[i])

for low, high in zip(A_low,A_high):
    print(low,high)

l1 = [3, 6, 1]; l2 = [1.5, 1, 0]; l3 = [9.1, 3, 2];
for e1, e2, e3 in zip(l1, l2, l3):
    print(e1, e2, e3)

A_low = [P*(1+2.5/100)**n for n in range(11)]
A_high = [P*(1+5.0/100)**n for n in range(11)]

amounts = [A_low, A_high] # list of two lists

print(amounts[0])       # the A_low list
print(amounts[1])       # the A_high list
print(amounts[1][2])    # the 3rd element in A_high

#   for sublist1 in somelist:
#       for sublist2 in sublist1:
#           for value in sublist2:
#               # work with value

#   for i1 in range(len(somelist)):
#       for i2 in range(len(somelist[i1])):
#           for i3 in range(len(somelist[i1][i2]))
#               # work with value

L = [[9, 7], [-1, 5, 6]]
for row in L:
    for column in row:
        print(column)

a = [2, 3.5, 8, 10]
a[2:]   # from index 2 to end of list
a[1:3]  # from index 1 up to, but not incl., index 3
a[:3]   # from start up to, but not incl., index 3
a[1:-1] # from index 1 to next last element
a[:]    # the whole list

# 3.6 Tuples
t = (2, 4, 6, 'temp.pdf')
t = 2, 4, 6, 'temp.pdf'
print(t)
t = t + (-1.0, -2.0)
print(t)
print(t[1])
print(t[2:])
print(6 in t)

# note that tuples are immutable, so functions like 
# t[1] = -1, t.append(0), and del t[1] don't work on it



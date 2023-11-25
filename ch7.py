# Section 7.1

# 'Norway' --> 'Oslo'
# 'Sweden' --> 'Stockholm'
# 'France' --> 'Paris'

def f(x):
    if x == 'Norway':
        return 'Oslo'
    elif x =='Sweden':
        return 'Stockholm'
    elif x == 'France':
        return 'Paris'

d = {'Norway':'Oslo', 'Sweden':'Stockholm','France':'Paris'}
print(d['Norway'])
print(d)
d['Germany'] = 'Berlin'
print(d)

#mydict = {'key1': value1, 'key2': value2,...}

temps = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5}

# or

# mydict = dict(key1 = value1, key2= value2)

temps = dict(Oslo = 13, London = 15.4, Paris = 17.5)

# for key in dictionary:
#     value = dictionary[key]
#     print value

temps = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5, 'Madrid': 26}

for city in temps:
    print(f'The {city} temperature is temps{city}')

for city in sorted(temps): # alphabetic sort of keys
    value = temps[city]
    print(value)


if 'Berlin' in temps:
    print('Berlin:', temps['Berlin'])
else:
    print('No temperature data for Berlin')

del temps['Oslo']   # remove Oslo key and value
print(temps)
print(len(temps))           # no of key-value pairs in dict.

for temp in temps.values():
    print(temp)

keys_list = list(temps.keys())

t1 = temps
t1['Stockholm'] = 10.0    # change t1
print(temps)
t2 = temps.copy()
t2['Paris']
t1['Paris']

L = [1, 2, 3]
M = L
M[1] = 8
print(M[1])
print(L[1])

M = L.copy()    # for lists, M = L[:] also works
M[2] = 0
print(M[2])
print(L[2])

d = {1: 34, 2:67, 3: 0 } # key is int
d = {13: 'Oslo', 15.4: 'London'} # possible
d = {(0,0): 4, (1, -1): 5}  # key is tuple
# d = {[0,0]: 4, [-1,1]: 5}   # list is mutable/changeable

# Section 7.2

p = {0:-1, 2:1, 7:3}

def eval_poly_dict(poly,x):
    sum = 0.0
    for power in poly:
        sum += poly[power]*x**power
    return sum

def eval_poly_dict(poly,x):
    # Python's sum can add elements of an interator
    return sum(poly[power]*x**power for power in poly)

p = [-1, 0, 1, 0, 0, 0, 0, 3]

def eval_poly_list(poly,x):
    sum = 0
    for power in range(len(poly)):
        sum += poly[power]*x**power
    return sum

def eval_poly_list_enum(poly,x):
    sum = 0
    for power, coeff in enumerate(poly):
        sum += coeff*x**power
    return sum

p = {-3: 0.5, 4:2}
print(eval_poly_dict(p,x = 4))

# Section 7.3

# Oslo: 21.8
# London: 18.1
# Berlin: 19
# Paris: 23
# Rome: 26
# Helsinki: 17.8

# with open('deg2.txt', 'r') as infile:
#   temps = {}                      # start with empty dict
#   for line in infile:
#       city, temp = line.split()
#       city = city[:-1]            # remove last char (:)--look at this code again
#       temps[city] = float(temp)

# Section 7.4

# Recall the split method:
s = 'This is a string'
print(s.split())
s = 'Berlin: 18.4 C at 4 pm'

print(s[0])
print(s[1])
print(s[-1])
print(s[-2])

print(s)
print(s[8:])    # from index 8 to the end of the string
print(s[8:12])  # index 8, 9, 10, and 11 (not 12!)
print(s[8:-1])
print(s[8:-8])

print(s)
for s_ in s:
    print(s_, end=' ')

print(s.find('Berlin'))     # where does 'Berlin' start?
print(s.find('pm'))         # at index 0
print(s.find('Oslo'))       # not found

print('Berlin' in s)
print('Oslo' in s)

if 'C' in s:
    print('C found')
else:
    print('no C')

print(s)
s.replace(' ', '__')
print(s)
s.replace('Berlin', 'Bonn')
print(s)
s.replace(s[:s.find(':')], 'Bonn')

print(s)
print(s.split(':'))
s.split()

strings = ['Newton', 'Secant', 'Bisection']
print(', '.join(strings))
print(' '.join(strings))

l1 = 'Oslo: 8.4 C at 5 pm'
words = l1.split()
l2 = ' '.join(words)
print(l1)
print(l2)
print(l1 == l1)

# Tromso Norway 69.6351 18.9920 52436
# Molde Norway 62.7483 7.1833 18594
# Oslo Norway 59.9167 10.7500 835000
# Stockholm Sweden 59.3508 18.0973 1264000
# Uppsala Sweden 59.8601 17.6400 133117

# cities = {}
# with open('cities.txt') as infile:
#     for line in infile:
#         words = line.split()
#         name = ', '.join(words[:2])
#         data = {'lat': float(words[2]), 'long': float(words[3])}
#         data['pop'] = int(words[4])
#         cities[name] = data

t= '1st line\n2nd line\n3rd line' # Unix
print(t)
print(t.split('\n'))    # Unix split
print(t.splitlines())   # Cross platform
t = '1st line\r\n2nd line\r\n3rd line' # Windows
print(t.splitlines())    # Cross platform

# build a new string by adding pieces of s:
s2 = s[:18] + '5' + s[19:]
print(s2)
s2 = s.replace(s[18],'5')
print(s2)

s = '      text with leading/traling space        \n'
print(s.strip())
print(s.lstrip())   # left strip
print(s.rstrip())   # right strip

print('214'.isdigit())
print('    214'.isdigit())
print('2.14'.isdigit())

print('     '.isspace())    # blanks
print('     \n'.isspace())  # newline
print('   \t '.isspace())   # TAB
print(''.isspace())         # emptry string

print(s.startswith('Berlin'))
print(s.endswith('am'))

print(s.lower())
print(s.upper())

# (1.3,0) (-1,2) (3,-1.5)
# (0,1) (1,0) (1,1)
# (0,-0.01) (10.5,-1) (2.5,-2.5)

# pairs = []  # list of (n1, n2) pairs of numbers
# with open('pairs.txt', 'r') as lines:
#     for line in lines:
#         words = line.split()
#         for word in words:
#             word = word[1:-1]  # strip off parentheses
#             n1, n2 = word.split(',')
#             n1 = float(n1); n2 = float(n2)
#             pair = (n1, n2)
#             pairs.append(pair)
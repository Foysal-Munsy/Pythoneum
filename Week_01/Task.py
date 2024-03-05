

# basic numeric operations
# 34 - 22
print(34-12)

# classic division returns a float
print(23/12)

# floor division discards the fractional part
print(23//7)

# assigin value to variable for later use
a = 1299
b= 22
print(a/b)
# print()

# use the variable a for further operations
a=99
b = a*9
print(b)

a=2 ** 10
print("2 ** 10 =",a)
# print(a)


# code here
a=10
b=5
print(a//b)



# importing the math module
import math
# accessing the constant π from math
print(math.e)
print(math.tau)
print(math.pi)

# using the method sqrt from math
print(math.sqrt(66))
x=10
y=5
print(math.pow(x,y))

math.factorial(5)
math.sin(120)

print(math.prod([2,3,5,7]))
print(sum([2,3,5,7]))
print(math.fsum([3,3,3]))


a=1
b=2
print(1+2)
print(a*4)
print(a/b)
print(a//b)


# code here
import datetime
store=datetime.datetime(2024,1,28)
now=datetime.datetime.now()
print("date & time that i store: ",a)
print("Current date & time: ",now)


a=10.5
print(a)

# Checking the type of an object
a = int(a)
b= float(b)
print(type(a))
print(type(b))

c = 123
print(type(c))
c = float(c)
print(type(c))

d = '123'
print(type(d))
d = "123"
print(type(d))
print(d[0])

c = 45.5
print(type(c))
c = str(c)
print(type(c))
print(c[3])

a = 7
d = 99.0+a
print(type(d))


# assign value to a variable. The value can be qouted using '' or ""
s = 'I love Bangladesh'
print(s)

# index
print(s[3])
print(s[9])

# negative index
s = 'asdf'
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])

"""When to use ' ' or " " ?

string operations with * and +
"""

print('Foysal ' * 8)
print('\n')
print("Lets try 10 times\n"*10)

greet='Hey'
greet * 3

name = 'Foysal ' + 'Munsy'
print(name)

greet + ',' + name + ' have you done your work?'

# slicing
name = 'Foysal Munsy'
print(name[0:6])
print(name[4:])
print(name[:4])
print(name[-3:])
print(name[0: :10])
print(name[-1: :-1])
name = "Hello, World!"
print(name[1:5:10])

name = 'Foysal Munsy'
name[-8:-2]

#dir(name)

"""Some examples of string methods"""

name = 'Foysal Munsy'
sub = 'y'
name.count(sub)

print(help(name.count))
#this help function generates a text on console

print(name.split()[-1])

name = "Hello, World!"
print(name.islower())  #False
print(name.isupper())  #False

name = "hello, world!"
print(name.islower())  #True
print(name.isupper())  #False

name = "HELLO, WORLD!"
print(name.islower())  #False
print(name.isupper())  #True

mystring = 'I am right\nHe is fine\nThis is okay'
print(mystring.splitlines())
print('\n')
print(mystring)

mystring ='I am right\nHe is fine\nThis is okay'
mystring.split(' ')

separator = '?? '
mystrings = ['first ', 'second ', 'third ', 'fourth ']
separator.join(mystrings)

#help(mystring.count)

print(len(name))

# check which functions you can use with variable 'name'
dir(name)

help(name.split)

"""<b>Exercise 3:</b> Demonstrate some string operations. Also, show uses of some string methods."""

# Code here
greet = 'Hello'
name = 'Foysal Munsy'
rep = greet * 3
print(rep)
print(name)
print(greet[0:5])
length1 = len(greet)
length2 = len(name)
print(length1)
print(length2)
low = greet.lower()
up = greet.upper()
title = greet.title()
print(low,up,title)

"""# List
<p style="text-align: justify">Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.</p>
"""

num = [1, 4, 9, 16, 25]
print(num)
name = ['Foysal','Nahid','Arif','Zahid','Arafat']
print(name)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
#list is a collection which is ordered and changeable
#They can contain any type of objects, like numbers, strings, and even other lists
"""
['Manager', 89000] its a list of list
21 int , 'Manager' string, 4.50 float
"""
data.insert(0,10)
print(data)

"""Like strings (and all other built-in sequence types), lists can be indexed and sliced:"""

data[-3][0]

data[-1]

data[0:3]

data[1]

data[2][0]

len(data)

data

"""Some list methods"""

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.append(100)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.insert(2,100)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.remove(4.5)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.pop(1)
print(data)

dir(data)

#help(data.insert)

"""Lists also support operations like concatenation"""

# greet = 'Hello'
name + data

"""<b> Exercise 4:</b> Implement stack using list
<p><b>Hints:</b> The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index</p>
"""

# code here
# LIFO
stack = []
stack.append('F')
stack.append('O')
stack.append('Y')
stack.append('S')
stack.append('A')
stack.append('L')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

"""<b> Exercise 5:</b> Implement queue using list
<p><b>Hints:</b> It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”)</p>
"""

# code here
queue = []
queue.append('F')
queue.append('O')
queue.append('Y')
queue.append('S')
queue.append('A')
queue.append('L')
print(queue)
queue.pop(0)
print(queue)
queue.pop(3)
print(queue)

"""# Dictionary
<p style="text-align: justify">Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.</p>

<p style="text-align: justify">It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.</p>
"""

tel = {'jack': 4098, 'sape': 4139}
print(tel)

list(tel.keys())[1]

tel['guido'] = 4127
tel

person = {'Age':21,'Name':['niaz','rahman'], 'Salary':56000, 'Rating':4.50}

person['Rating']

len(person)

person.keys()

#person.has_key('Name')
'Name' in person.keys()

'niaz' in person['Name']

#dir(person)

"""<b> Exercise 6:</b> Define a dictionary to store the details of persons. Also, print some data from the dictionary.
 <p><b>Hint:</b> You may require nesting dictionary, lists, string inside the dictionary.</p>
"""

# Code here
students = {
    'Foysal':{'Id':'22-47225-1' , 'Home town':'Chandpur', 'Semester':'7th', 'Interests':['Cricket', 'Football']},
    'Zahid':{'Id':'21-47225-3' , 'Home town':'Chandpur', 'Semester':'8th', 'Interests':['Cricket', 'Carom']},
    'Mahi':{'Id':'22-47300-1' , 'Home town':'Dhaka', 'Semester':'7th', 'Interests':['Gaming', 'Football']}
}
print(students)
print("\nFoysal's Id:", students['Foysal']['Id'])

"""# Tuples and Sets
<b>Exercise 7: (Optional)</b> Use the content from [here](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) to follow some examples on tuple and set.
"""

# code from here
t = 12345, 54321, 'hello!'
print("t[0]:", t[0])
print("t:", t)

u = t, (1, 2, 3, 4, 5)
print("u:", u)
try:
    t[0] = 88888
except TypeError:
    print('not possible')

v = ([1, 2, 3], [3, 2, 1])
print("v:", v)

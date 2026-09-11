"""import my_module

chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = my_module.find_index(chicks, 'emo')
print(index)"""

"""import my_module as mm #imported as mm

chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = mm.find_index(chicks, 'emo')
print(index)"""

"""from  my_module import  find_index #function directly imported
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(index)"""
"""
from  my_module import  find_index, test #to import other things 
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(index)
print(test)"""


"""from  my_module import  find_index as fi, test #to import as a name
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = fi(chicks, 'emo')
print(index)
print(test) """

"""from  my_module import * #to import everything directly but confusion arises as what got imported  
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(index)
print(test) """

"""from  my_module import  find_index, test #to import other things 
import sys # to find path
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

index = find_index(chicks, 'emo')
print(sys.path)"""

"""import random #random module
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

random_chick= random.choice(chicks)
print(random_chick)"""

"""import math #for mathematical operations
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

rads = math.radians(60)
print(rads)
print(math.sin(rads))"""

"""import datetime #for date and time operations
import calendar #for calendar things
chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']

today = datetime.date.today()
print(today)
print(calendar.isleap(2024))"""

"""import os # os info and access to files 
print(os.getcwd()) #location of directory
print(os.__file__) # location of file """

"""import requests

response = requests.get("https://example.com")

print(response.status_code)"""

'''
LEGB
Local, Enclosing, Global, Built-in
'''
# x = 'global x' # x in global scope 

"""def test(): #test function
    global x #changing the global x if we remove it now we are setting just locally ..and print(x) outside test function will throw an error 
    #y= 'local y'  #y in local scope 
    x ='local x' # local x function and anything outside this local scope sees the global scope 
    #print(y)
    print(x) #print x within the test function 

test()
#print(y) # error will occur because y doesn't live outside the test function and doesn't find local, global, enclosing, built-in scope 
print(x)  """ 

'''def test(z): #local variable in this function 
    x ='local x' # local x function and anything outside this local scope sees the global scope 
    print(z) #print x within the test function 
test('local z')'''

# built in scope 
'''import builtins

print(dir(builtins))
m = min([10, 30, 56, 28, 97])
print(m)'''

'''def outer():
    x = 'outer x' #local variable to outer function 

    def inner():
        x = 'inner x' #local variable to inner function 
        print(x)

    inner()
    print(x)

outer()'''

'''def outer():
    x = 'outer x' #local variable to outer function 

    def inner():
        print(x) # outer x will be printed as no local variable thus thiw will look to enclosing function 

    inner()
    print(x)

outer()'''

'''def outer():

    def inner():
        x = 'inner x' #local variable to inner function 
        print(x) #printed out x with our inner function because it has local variable in the inner function 

    inner()
    print(x) # would force an error because no local variable is here and no enclosing function in the enclosing scope 

outer()'''

'''def outer():
    x = 'outer x' #local variable to outer function 

    def inner():
        nonlocal x # would allow us to work local variables of enclosing functions which means we are affecting the x variable of the outer function 
        x = 'inner x' #now it is affecting local x of our enclosing function and would print out inner x within this inner function 
        print(x)

    inner()
    print(x) #inner x overwritten here 

outer() '''

x = 'global x'


'''def outer():
    x = 'outer x' #local variable to outer function 

    def inner():
        x = 'inner x' #local variable to inner function 
        print(x)

    inner()
    print(x)

outer()
print(x)'''

'''def outer():
    #x = 'outer x' #local variable to outer function 

    def inner():
        #x = 'inner x' #local variable to inner function 
        print(x)

    inner()
    print(x)

outer()
print(x)'''

#slicing 

'''num = [1,2,3,4,5,6,7,8,9]
# list[ start:end:step]

print(num[3:-2:2])
print(num[0:-1:2])
print(num[-1:2:-1])

'''
'''nuts = 'suck deez_nuts blud'
print(nuts)
print(nuts[:10])'''

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print (my_list)

print([n for n in nums])

# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
   my_list.append(n*n)
print (my_list)

my_list = [n*n for n in nums]
print(my_list)

# Using a map + lambda
my_list = map(lambda n: n*n, nums)
print (list(my_list))

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
       my_list.append(n)
print (my_list)

my_list = [n for n in nums if n%2==0]
print(my_list)

# Using a filter + lambda
my_list = filter(lambda n: n%2 == 0, nums)
print (list(my_list))

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
     my_list.append((letter,num))
print (my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print (zip(names, heros))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
     my_dict[name] = hero
print (my_dict)

my_dict = {name:hero for name, hero in zip (names, heros) if name != 'Peter'}
print(my_dict)


# If name not equal to Peter

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print i
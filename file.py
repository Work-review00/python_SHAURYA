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

'''nums = [1,2,3,4,5,6,7,8,9,10]

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

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print (my_set)


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
     for n in nums:
         yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print (i)'''

#sorting lists, tuple, objects

'''li = [3, 5, 9, 19, 38, 29, 11, 68, 45, 89]

s_li = sorted(li)

print(' sorted variable :', s_li)
print('original variable:', s_li) 
print('original variable:', li)

li.sort()  # sorting the list through sort() method in ascending order 
print('original variable:', li) #gets sort because of the sort method 

s_li= sorted(li, reverse=True )
print(' sorted variable :', s_li)'''

'''tup = [3, 5, 9, 19, 38, 29, 11, 68, 45, 89]
s_tup = sorted(tup)
print('tuple:', s_tup)'''

'''di = {'name': 'Tony Stark', 'alias' : 'Iron Man', 'designation': 'saving the universe'}
s_di = sorted(di)
print('Dict:', s_di) #keys gets sorted in alphabetical order '''

'''li= [ -6,-5,-4,1,2,3 ]
s_li = sorted(li)
print(s_li)

s_li= sorted(li, key= abs) #gives out absolute values 
print(s_li)'''

#sorting objects

'''class Employee():
    def __init__(self, name, age, salary ):
        self.name = name
        self.age = age
        self.salary = salary 

    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age, self.salary)


#from operator import attrgetter

e1 = Employee('Luke', 30, 50000)
e2 = Employee('Ronn', 32, 80000)
e3 = Employee('Ben',  28, 45000)

employees= [e1,e2,e3]

def e_sort(emp):
    return emp.name #could change for age and salary 

s_employees = sorted(employees, key = e_sort)
# s_employees = sorted(employees, key = e_sort, reverse= True) #to reverse the order 
#s_employees = sorted(employees, key = lambda e: e.age) sorting through lambda and then no need of e_sort function 
#s_employees = sorted(employees, key = attrgetter ('age')) #sorting directly through attrgetter 
print(s_employees)'''


#string formatting 

'''person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)


sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

l = ['Jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(sentence)



tag ='h1'
text = 'this is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)'''

'''class Person():

    def __init__(self, name, age ):
        self.name = name
        self.age = age

pl = Person('Klaus', '133')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(pl)
print(sentence)'''

'''sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age= '35')
print(sentence)


person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)
 '''

'''for i in range(1,11):
    # sentence = 'This value is {}'.format(i)
    sentence = 'This value is {:03}'.format(i)
    print(sentence)'''

'''pi = 3.14159265

#sentence = 'Pi is equal to {}'.format(pi)
sentence = 'Pi is equal to {:.2f}'.format(pi) #upto 2 decimal places
print(sentence)'''

'''#sentence = '1 MB is equal to {:,} bytes'.format(1000**2) #comma separators
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)'''

#string formatting in dateandtime 
'''import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)

#sentence = '{}'.format(my_date)
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j } day of the year'.format(my_date)

print(sentence)'''


#working with os module 
#import os 
'''#print(dir(os)) #shows all attributes and methods we have access to in this module
#print(os.getcwd())
#os.chdir() #used to change directory
#print(os.listdir()) #list of files and folders in the current directory

#os.mkdir()  #used to create a new directory 
#os.makedirs('ye_da_goat') #used to create a new directory but it works deep 
#os.rmdir() #to remove directory 
#os.removedirs('ye_da_goat') 
#os.mkdir('test.txt')
# os.rename('test.txt', 'demo.txt')
# print(os.stat('demo.txt'))
#print(os.stat('demo.txt').st_size)  
#print(os.stat('demo.txt').st_mtime)  

from datetime import datetime
mod_time = (os.stat('demo.txt').st_mtime) 
print(datetime.fromtimestamp(mod_time))''' 

#import os 
'''for dirpath, dirnames, filenames in os.walk(r 'F:\\pythondev\\demo.txt'): #to see the directory tree
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()'''


#print(os.environ)
'''for key, value in os.environ.items():
    print(key, '=', value)'''

#print(os.environ.get('VIRATV'))
'''import os

#print(os.environ.get('USERPROFILE'))

'test.txt'

#file_path = os.environ.get('USERPROFILE') + 'test.txt'  #faulty method
file_path = os.path.join(os.environ.get('USERPROFILE') , 'test.txt' )
print(file_path)
'''

#import os
'''
print(os.path.basename('/tmp/text.txt'))
print(os.path.dirname('/tmp/text.txt'))
print(os.path.split('/tmp/text.txt'))
print(os.path.exists('/tmp/text.txt'))
print(os.path.isdir('/tmp/text.txt'))
print(os.path.isfile('/tmp/text.txt'))
print(os.path.splitext('/tmp/text.txt'))
'''

#print(dir(os.path))

#datetime module


'''import datetime

d = datetime.date(2023,5, 20) #month should not start with 0 as it would force an error  
print(d)

tday= datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday()) #monday 0 sunday 6
print(tday.isoweekday()) #monday 1 sunday 7

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

#date2 = date1 + timedelta
#timedelta = date + date 2

bday= datetime.date(2027, 1, 2)

till_bday = bday- tday 
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())'''

'''import datetime

t= datetime.time(4,45,57,500000)
print(t.hour)

dt= datetime.datetime(2023,11,26,6,38,42,300000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7)
print(dt + tdelta )'''

'''import datetime

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)'''

'''import datetime
import pytz

dt = datetime.datetime(2021, 8, 23, 11, 35, 50, tzinfo=pytz.UTC)
print(dt)

#dt_today = datetime.datetime.today(tz=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

#print(dt_today)
print(dt_now)
print(dt_utcnow)'''

'''import datetime
import pytz


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_ist = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ist)

for tz in pytz.all_timezones:
    print(tz)'''

'''import datetime

dt_utcnow = datetime.datetime.now(datetime.UTC)

dt_ist = dt_utcnow.astimezone(
    datetime.timezone(datetime.timedelta(hours=5, minutes=30))
)

print(dt_ist)'''

'''import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = datetime.datetime.now()
dt_east= dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)
print(dt_east)'''

'''import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
#print(dt_utcnow)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)

dt_east= dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)'''


'''import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
#print(dt_mtn.isoformat()) 
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime'''
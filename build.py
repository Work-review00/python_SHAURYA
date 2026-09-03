#strings

"""quote= "this world just sucks the soul out of you."
print(len(quote)); #length
print(quote[0:4]); #range
print(quote[9]); #length
print(quote[-1]); #last character
print(quote[:4] + quote[-1]); #range and last character
print(quote[9:]); #range from index 9 to end
print(quote.lower()); #convert to lowercase
print(quote.upper()); #convert to uppercase
print(quote.replace("sucks", "drains")); #replace word
print(quote.split(" ")); #split by space
print(quote.find("sucks")); #find index of word
print(quote.count("sucks")); #count occurrences of word"""

aim= "to become the best dev"
execution= "you have to show up every day and put in the work"

"""goal= aim + " " + execution + ". gotcha! " #string concatenation
print(goal)

goal='{},{}. gotcha!'.format(aim, execution) #string formatting
print(goal)

goal= f"{aim}, {execution}. gotcha!" #f-string formatting
print(goal)

goal= f"{aim.upper()}, {execution.lower()}. gotcha!" #f-string formatting with case conversion
print(goal)

print(dir(aim)) #list of attributes and methods of the string object"""

#print(help(str)) #help documentation for string methods
# print(help(str.replace)) #help documentation for the replace method

"""aim="to become the best dev"
print(aim.startswith("to")) #check if string starts with "to"
print(aim.endswith("dev")) #check if string ends with "dev"

print(aim.isalpha()) #check if string contains only alphabetic characters
print(aim.isdigit()) #check if string contains only digits

print(aim.strip()) #remove leading and trailing whitespace
print(aim.split()) #split string into a list of words
print(aim.join(["I want ", " and I will"])) #join a list of strings with the aim string as separator

print(aim.center(50, "-")) #center the string with padding"""

#integers and floats

"""int1= 10
int2= 3    
num1= 10.5
num2= 3.2
print(int1 + int2) #addition
print(int1 - int2) #subtraction
print(int1 * int2) #multiplication
print(int1 / int2) #division
print(int1 % int2) #modulus
print(int1 ** int2) #exponentiation
print(int1 // int2) #floor division
print(int1 > int2) #greater than
print(int1 < int2) #less than   
print(int1 == int2) #equal to
print(int1 != int2) #not equal to
print(int1 >= int2) #greater than or equal to
print(int1 <= int2) #less than or equal to
print(int1 + num1) #addition with float
print(int1 - num1) #subtraction with float
print(int1 * num1) #multiplication with float
print(int1 / num1) #division with float
print(int1 % num1) #modulus with float
print(int1 ** num1) #exponentiation with float
print(int1 // num1) #floor division with float"""

#lists

"""chicks= ['alts', 'goths', 'emo', 'punks', 'hippies', 'mommies', 'cougars', 'milfs', 'grannies', 'babes', 'ladies']
print(chicks)
print(len(chicks)) #length of the list
print(chicks[0]) #first element
print(chicks[-1]) #last element
print(chicks[2:5]) #range of elements
print(chicks[:3]) #first three elements #slicing
print(chicks[3:]) #elements from index 3 to end
chicks.append('curvy') #adding element
print(chicks)
chicks.insert(0, 'snowbunnies') #adding element at specific index
print(chicks)

chicks_2 = ['blonde', 'brunette', 'redhead']
chicks.insert(0, chicks_2[0]) #adding element from another list at specific index
print(chicks)
chicks.insert(0, chicks_2) #adding element from another list at specific index
print(chicks)
print(chicks[0]) #first element of the revised list

chicks_2 = ['blonde', 'brunette', 'redhead'] #another list
chicks.extend(chicks_2) #extending another list into original one
print(chicks)

chicks.remove('blonde') #removing an element 
print(chicks)
chicks.pop() #popping the element  by default last 
popped = chicks.pop()
print(popped) #popped element
print(chicks) 

chicks.reverse() #reversing the list
print(chicks)

chicks.sort() #sorting the list in ascending order
print(chicks)

numbers = ['5', '2', '8', '1', '9']
numbers.sort()
print(numbers)

chicks.sort(reverse=True) #sorting the list in descending order
print(chicks)

numbers.sort(reverse=True) #sorting the list in descending order
print(numbers)

sorted_chicks = sorted(chicks) #sorting the list in ascending order without changing the original list
print(sorted_chicks)

print(chicks) #original list remains unchanged

print(min(chicks)) #minimum element in the list
print(max(chicks)) #maximum element in the list

nums = [5, 2, 8, 1, 9]
print(min(nums)) #minimum element in the list
print(max(nums)) #maximum element in the list
print(sum(nums)) #sum of the elements in the list
 
print(chicks.index('emo')) #index of an element in the list
print(chicks.count('emo')) #count of an element in the list
#print(chicks.index('sweetgirlies')) #index of an element in the list

print('sweetgirlies' in chicks) #check if an element is in the list
print('emo' in chicks) #check if an element is in the list   

for item in chicks: #iterating through the list
    print(item)

for index, item in enumerate(chicks): #iterating through the list with index
    print(index, item) 

for index in range(len(chicks)): #iterating through the list with index
    print(index, chicks[index])

for index in enumerate(chicks, start=1): #iterating through the list with index starting from 1
    print(index)

chicks_str = ', '.join(chicks) #joining the list into a string
print(chicks_str)

chicks_list = chicks_str.split(', ') #splitting the string back into a list
print(chicks_list)"""

#tuples
"""
coordinates = (4, 5) #tuple
print(coordinates[0]) #first element of the tuple
print(coordinates[1]) #second element of the tuple

#IMMUTABLE: tuples cannot be changed after creation

#SETS

colors = {'red', 'green', 'blue'} #set
print(colors)

empty_set = set() #empty set

#dictionaries

cricketer = {'name': 'Virat Kohli', 'age': 32, 'team': 'India'} #dictionary
print(cricketer['name']) #accessing value by key
print(cricketer['age']) #accessing value by key
print(cricketer['team']) #accessing value by key
print(cricketer.get('name')) #accessing value by key using get method
print(cricketer.get('age')) #accessing value by key using get method
print(cricketer.get('team')) #accessing value by key using get method 

cricketer['age'] = 33 #updating value by key
print(cricketer)

cricketer['country'] = 'India' #adding new key-value pair
print(cricketer)

cricketer.update({'age': 34, 'team': 'India'}) #updating multiple key-value pairs
print(cricketer)

del cricketer['team'] #deleting key-value pair by key
print(cricketer)  

team = cricketer.pop('team', None) #deleting key-value pair by key and returning the value
print(team) #returns None since 'team' key is not present in the dictionary

age= cricketer.pop('age') #deleting key-value pair by key and returning the value
print(age) #returns the value of the 'age' key and removes it from the dictionary

print(len(cricketer)) #length of the dictionary

print(cricketer.keys()) #list of keys in the dictionary
print(cricketer.values()) #list of values in the dictionary
print(cricketer.items()) #list of key-value pairs in the dictionary

for key, value in cricketer.items(): #iterating through the dictionary
    print(key, value)

for key in cricketer.keys(): #iterating through the dictionary keys
    print(key)

for value in cricketer.values(): #iterating through the dictionary values
    print(value)"""    

#conditional statements

"""age = 25
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are not an adult.")

user = "admin"
logged_in = False
if user == "admin" and logged_in:
    print("Welcome, admin!")
elif user == "admin" and not logged_in:
    print("Please log in to continue.")
elif user != "admin" and logged_in:
    print("Welcome, user!")
elif user == "admin" or logged_in:
    print("welcome, user!")
else:
    print("error: invalid user or not logged in.")"""

"""a = [1,2,3,4,5]
b = [1,2,3,4,5]
c= a
print(a is b) #False, because they are different objects in memory
print(a == b) #True, because they have the same values
print(c is a) #True, because c refers to the same object as a

print(id(a)) #memory address of a
print(id(b)) #memory address of b
print(id(c)) #memory address of c"""

"""conditional statements

condition = True
if condition:   
    print("Condition is True")
else:
    print("Condition is False")

condition = False
if condition:  
    print("Condition is True") 
else:
    print("Condition is False")

condition = None
if condition:
    print("Condition is True")
else:
    print("Condition is False")

condition = 0 #0 is considered False in Python
if condition:
    print("Condition is True")
else:
    print("Condition is False")

condition = 1 #any non-zero number is considered True in Python
if condition:
    print("Condition is True")
else:
    print("Condition is False")

condition = "" #empty string is considered False in Python
if condition:
    print("Condition is True")  
else:
    print("Condition is False")

condition = {} #empty list,dictionary,tuple is considered False in Python
if condition:
    print("Condition is True")
else:
    print("Condition is False")"""

nums= [1, 2, 3, 4, 5]
for num in nums:
    print(num) #prints each number in the list

numbers= [0,10,20,30,40,50]
for i in numbers:
    if i == 30:
        print("Found 30!") #prints when i is 30
        break #breaks the loop when i is 30
    #continue #skips the rest of the loop when i is 30  
    print(i) #prints each number in the list until 30

points = [11, 22, 33, 44, 55]
for point in points:
    if point == 33:
        print("Found 33!") #prints when point is 33
        continue #skips the rest of the loop when point is 33
    print(point) #prints each number in the list until 33

clubs = ['Manchester United', 'Real Madrid', 'Barcelona', 'Bayern Munich', 'Juventus']
for club in clubs:
    for letter in 'abcd':
        print(club, letter) #prints each club with each letter in 'abcd'
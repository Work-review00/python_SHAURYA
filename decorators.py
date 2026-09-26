'''def my_decorator(func):

    def wrapper():
        print("Starting...")

        func()

        print("Finished!")

    return wrapper


@my_decorator
def say_hello():
    print("Hello Boss")


say_hello()'''

'''def outer_function():
    message = 'HI'   #local variable

    def inner_function():   #inner function has access to local variable
        print(message)
    return inner_function() #executing the inner function 

outer_function() '''

'''
def outer_function():
    message = 'HI'   #local variable

    def inner_function():   #inner function has access to local variable
        print(message)
    return inner_function   #waiting to be executed 

outer_function() '''



'''def outer_function():
    message = 'HI'   #local variable

    def inner_function():   #inner function has access to local variable
        print(message)
    return inner_function   #waiting to be executed 

my_func= outer_function() #my func is our inner function waiting to be executed
my_func()   #inner function remembering the message variable even after outer_function has finished executing 
my_func()
my_func()
my_func()'''


'''def outer_function(msg):  #msg argument 
    message = msg   #local variable

    def inner_function():  
        print(message)
    return inner_function   


hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func()'''


'''def outer_function(msg):  #msg argument 
    def inner_function():  
        print(msg)
    return inner_function   


hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func()'''



'''def decorator_function(original_function):
    def wrapper_function():  
        return original_function()
    return wrapper_function   

def display():
    print('display function ran')


decorated_display = decorator_function(display)   # display = original function

decorated_display()'''


#decorating our functions allows us to easily add functionality to our existing functions by adding that functionality inside of our wrapper so for example here without modifying our original display function in any way I can come insdie of our wrapper and add any kind of code that I want 


'''def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function   

def display():
    print('display function ran')


decorated_display = decorator_function(display)  

decorated_display()'''


'''def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function   



@decorator_function   #having this syntax would be the same thing as saying thaat I want my display = decorator_function(display)
def display():
    print('display function ran')


decorated_display = decorator_function(display)  

decorated_display()'''


'''def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function   



@decorator_function   #having this syntax would be the same thing as saying thaat I want my display = decorator_function(display)
def display():
    print('display function ran')


display()  #still we will have the wrapper code added to our original function '''


'''
def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function   



@decorator_function   
def display():
    print('display function ran')


def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)

display()  '''



'''
def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function   



@decorator_function   
def display():
    print('display function ran')


def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)
'''


'''
def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function   



@decorator_function   
def display():
    print('display function ran')


@decorator_function   
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)  '''  

#we will get an error as after decoration 
#because after decoration display_info = decorator_function(display_info)
#display_info now points to wrapper_function
# so : display_info('John', 25) becomes: wrapper_function('John', 25)
# but wrapper says def wrapper_function():  ....
#It doesn't accept name and age.

#And this is exactly why decorators eventually use *args and **kwargs


'''
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function   



@decorator_function   
def display():
    print('display function ran')


@decorator_function   
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)  '''


'''
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function   

@decorator_function   
def display():
    print('display function ran')


@decorator_function   
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)  

display()'''

#using class to decorate 
'''
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function   


class decorator_class(object):

    def __init__(self, original_function):     #passing original function into this class 
        self.original_function = original_function   #going to tie our function with the instance of this class 

    def __call__ (self, *args, **kwargs ):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


    
@decorator_class   
def display():
    print('display function ran')


@decorator_class 
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)  

display()'''


#logging

'''
def my_logger(orig_func):
    import logging 
    logging.basicConfig(filename= '{}.log'.format(orig_func.__name__), level= logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger   
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)  '''



'''
def my_logger(orig_func):
    import logging 
    logging.basicConfig(filename= '{}.log'.format(orig_func.__name__), level= logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger   
def display_info(name,age):
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('love', 25) 

'''


#we can use this decorator anytime we want to add that logging functionality to any new function so we can imagine how repetitive 
#and error prone it would be if we wanted to add that fucntionality to multiple functions and tried to manually add in that logging code
#within each individual function The decorator allows us to maintain our added functionality in one location and easily apply it
#anywhere that we want within our codebase 

'''
def my_logger(orig_func):
    import logging 
    logging.basicConfig(filename= '{}.log'.format(orig_func.__name__), level= logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


import time

@my_timer   
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)  
'''


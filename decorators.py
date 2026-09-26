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


def decorator_function(original_function):
    def wrapper_function():  
        print('wrapper executed this before ' )
        return original_function()
    return wrapper_function   

def display():
    print('display function ran')


decorated_display = decorator_function(display)  

decorated_display()
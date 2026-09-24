'''def numbers():
    yield 1
    yield 2
    yield 3

print(numbers) #will give the generators object'''


'''def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
'''

'''def numbers():
    yield 1
    yield 2
    yield 3

x = numbers()

print(next(x))
print(next(x))
print(next(x))
print(next(x)) #stop iteration ..generator end no more values'''


'''def numbers():
    for i in range(1, 1000001):
        yield i

for num in numbers():
    print(num)'''

# list
'''def square_numbers(nums):
     result = []
     for i in nums:
          result.append(i*i)
     return result

my_nums = square_numbers([1,2,3,4,5])

# my_nums = (x*x for x in [1,2,3,4,5])

print (my_nums) # [1, 4, 9, 16, 25]

#for num in my_nums:
 #   print (num)'''

#transformed into generators  

'''def square_numbers(nums):
     for i in nums:
          yield(i*i) #will print generator object , generator doesn't hold entire thing in memory, yields one result at a time whereas list hold everything in the memory

my_nums = square_numbers([1,2,3,4,5])

# my_nums = (x*x for x in [1,2,3,4,5])

#print (my_nums) # [1, 4, 9, 16, 25] # generator object as outcome 
print (next(my_nums)) #will give one value at a time in order 
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))'''


def square_numbers(nums):
     for i in nums:
          yield(i*i) 

# my_nums = square_numbers([1,2,3,4,5])

my_nums = (x*x for x in [1,2,3,4,5])

print(my_nums) #will give genrator object 

print(list(my_nums)) # will make a list from the genrators

for num in my_nums:
    print(num)
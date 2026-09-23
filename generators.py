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


def square_numbers(nums):
     result = []
     for i in nums:
          result.append(i*i)
     return result

my_nums = square_numbers([1,2,3,4,5])

my_nums = (x*x for x in [1,2,3,4,5])

print (list(my_nums)) # [1, 4, 9, 16, 25]

for num in my_nums:
    print (num)
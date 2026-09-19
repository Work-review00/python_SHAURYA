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


def numbers():
    for i in range(1, 1000001):
        yield i

for num in numbers():
    print(num)
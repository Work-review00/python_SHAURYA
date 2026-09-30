'''class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(self.brand, "is driving")

    def stop(self):
        print(self.brand, "has stopped")


car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

print(car1.brand)
print(car2.brand)

car1.drive()
car2.drive()

car1.stop()
car2.stop()'''



'''
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Balance:", self.balance)

account1 = BankAccount("Rahul", 5000)

account1.deposit(2000)

account1.withdraw(1000)

account1.show_balance()'''


'''
class Employee:

    company = "ABC Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def show_info(self):
        print(self.name, self.salary)

    # Class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

   # Create objects:

employee1 = Employee("Rahul", 50000)
employee2 = Employee("Aman", 60000)

#Instance method:

employee1.show_info()

#Class method:

Employee.change_company("XYZ Ltd")

#Static method:

print(Employee.is_valid_salary(50000))'''



'''
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()
emp_3 = Employee()

print(emp_1)   #will give employee object location
print(emp_2)   #will give employee object location
print(emp_3)   #will give employee object location


emp_1.first = 'Jon'
emp_1.last = 'Snow'
emp_1.email = 'jonsnow@winteriscoming.com'
emp_1.pay = 80000

emp_2.first = 'Ned'
emp_2.last = 'Stark'
emp_2.email = 'nedstark@winteriscoming.com'
emp_2.pay = 60000

emp_3.first = 'Robb'
emp_3.last = 'Stark'
emp_3.email = 'robbstark@winteriscoming.com'
emp_3.pay = 100000


print(emp_1.email)
print(emp_2.email)
print(emp_3.email)'''


'''
class Employee:

    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@winteriscoming'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jon', 'Snow', 80000)
emp_2 = Employee('Ned','Stark', 60000)
emp_3 = Employee('Robb', 'Stark',100000)

print(emp_1.email)
print(emp_2.email)
print(emp_3.email)

print(emp_1.fullname())   #will give naame 
print(Employee.fullname(emp_2))  #will give name'''


'''
class Employee:

    raise_amount = 1.04    #class variable

    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@winteriscoming'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int( self.pay * 1.04) # no need when class variable 
        # self.pay = int( self.pay * raise_amount) #throws an error

        #self.pay = int( self.pay * Employee.raise_amount) #both works
        self.pay = int( self.pay * self.raise_amount) #both works
        


emp_1 = Employee('Jon', 'Snow', 80000)
emp_2 = Employee('Ned','Stark', 60000)
emp_3 = Employee('Robb', 'Stark',100000)

# print(emp_1.__dict__) 

#print(Employee.__dict__) 

#Employee.raise_amount = 1.05

emp_1.raise_amount = 1.05

print(emp_1.__dict__) 

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)

# emp_1.raise_amount
# Employee.raise_amount
'''


class Employee:

    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@winteriscoming'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


print(Employee.num_of_emps)

emp_1 = Employee('Jon', 'Snow', 80000)
emp_2 = Employee('Ned','Stark', 60000)
emp_3 = Employee('Robb', 'Stark',100000)

print(Employee.num_of_emps)
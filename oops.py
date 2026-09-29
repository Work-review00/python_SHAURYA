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

account1.show_balance()
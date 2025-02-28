# # Practicing a simple class
# class Car:

#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print(f"The {self.make} {self.model} engine is running")


# car = Car(1990,"honda",2021)
# print (car.start_engine())


# class BankAccount:
#     def __init__(self, initial_balance):
#         self._balance = initial_balance

#     @property
#     def balance(self):
#         return self._balance

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print("Insufficient funds.")

# account = BankAccount(1000)
# print(account.balance)  # Output: 1000
# account.deposit(500)
# print(account.balance)  # Output: 1500

# Creating Metaclass

class Car(type):
    def __new__(cls,name,base,attr):
     
        if 'name' not in attr:
                raise Exception(f"if 'name' attribute not found in{name} not found")
        else:
            return super().__new__(cls,name,base,attr)
        

class Manual(metaclass=Car):
     name = "honda"

car = Manual()
print(car.name)

            
            



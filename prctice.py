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

# class Car(type):
#     def __new__(cls,name,base,attr):
     
#         if 'name' not in attr:
#                 raise Exception(f"if 'name' attribute not found intes{name} not found")
#         else:
#             return super().__new__(cls,name,base,attr)
        

# class Manual(metaclass=Car):
#      name = "honda"

# car = Manual()
# print(car.name)

            
# Practicing Inheritance

# class Parent:

#     def __init__(self,name):
#         self.name = name

# class Child(Parent):

#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age

# c = Child("Abubakr", 27)
# print (c.name)

# Practicing method inheritance

# class Parent:

#     def greet(self):
#         return "Hello from parents"

# class Child(Parent):

#     def greet(self):
#         parent_message = super().greet()
#         return (f"{parent_message} and Hello from child")


# c=Child()
# print (c.greet())

#Practicing Polymorphsim

# class Car:

#     def __init__(self,name,model):
#         self.name = name
#         self.model = model

# class Bikes:
    
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model


# c = Car("honda",2025)
# b = Bikes("yamaha",2024)

# print (c)
# print (b)
    

#Incapsulation

class Student:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age= age


s = Student("Alice", 20)
print (s.get_age())
s.set_age(45)
print(s.get_age())

    
        

            



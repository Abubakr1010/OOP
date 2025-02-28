class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model} engine is running")


car = Car(1990,"honda",2021)
print (car.start_engine())



# Parent class
class Vehicle:
    def start(self):
        print("Vehicle starts")

# Child class Car overriding start()
class Car(Vehicle):
    def start(self):
        print("Car starts with key")

# Child class Bike overriding start()
class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")


# Example usage
vehicles = [Vehicle(), Car(), Bike()]

for v in vehicles:
    v.start()   # Polymorphism in action

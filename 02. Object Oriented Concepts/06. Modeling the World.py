class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def drive(self):
        return "Car is driving"

class Boat(Vehicle):
    def sail(self):
        return "Boat is sailing"

class Stromberg(Car, Boat):
    pass

amphibious_vehicle = Stromberg()
print(amphibious_vehicle.drive())  # Car is driving
print(amphibious_vehicle.sail())   # Boat is sailing

class Vehicle:
    """Base class for all vehicles"""
    
    def _init_(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
    
    def move(self):
        """Base move method - to be overridden by subclasses"""
        return f"{self.name} is moving"
    
    def accelerate(self, amount):
        """Increase speed"""
        self.current_speed = min(self.max_speed, self.current_speed + amount)
        return f"Accelerating to {self.current_speed} km/h"
    
    def brake(self, amount):
        """Decrease speed"""
        self.current_speed = max(0, self.current_speed - amount)
        return f"Slowing down to {self.current_speed} km/h"
    
    def _str_(self):
        return f"{self.name} (Max: {self.max_speed} km/h)"

# Different vehicle types with polymorphic move() method
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road 🚗"
    
    def honk(self):
        return "Honk! Honk! 🚙"

class Plane(Vehicle):
    def move(self):
        if self.current_speed > 200:
            return f"{self.name} is flying in the air ✈"
        else:
            return f"{self.name} is taxiing on runway 🛫"
    
    def takeoff(self):
        self.current_speed = 300
        return "Taking off! ✈"

class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on water ⛵"
    
    def anchor(self):
        self.current_speed = 0
        return "Dropping anchor! ⚓"

class Bicycle(Vehicle):
    def move(self):
        return f"{self.name} is pedaling on the path 🚴"
    
    def ring_bell(self):
        return "Ring! Ring! 🔔"

class Rocket(Vehicle):
    def move(self):
        if self.current_speed > 1000:
            return f"{self.name} is launching into space 🚀"
        else:
            return f"{self.name} is preparing for launch 🛰"
    
    def launch(self):
        self.current_speed = 5000
        return "3...2...1... Liftoff! 🚀"

# Demonstration
print("\n=== VEHICLE POLYMORPHISM DEMONSTRATION ===\n")

# Create different vehicles
vehicles = [
    Car("Sports Car", 300),
    Plane("Jet Airplane", 900),
    Boat("Speedboat", 120),
    Bicycle("Mountain Bike", 40),
    Rocket("SpaceX Rocket", 28000)
]

# Test polymorphism - same method, different behavior
for vehicle in vehicles:
    print(vehicle.move())
    print(vehicle.accelerate(100))
    print(vehicle.move())
    print(vehicle.accelerate(200))
    print(vehicle.move())
    print(vehicle.brake(150))
    print("-" * 40)

# Special methods for specific vehicle types
print("\n=== SPECIAL METHODS ===\n")
car = Car("Family Car", 180)
plane = Plane("Boeing 747", 900)
boat = Boat("Yacht", 80)
bike = Bicycle("City Bike", 30)
rocket = Rocket("Satellite Launcher", 28000)

print(car.honk())
print(plane.takeoff())
print(plane.move())
print(boat.anchor())
print(bike.ring_bell())
print(rocket.launch())
print(rocket.move())
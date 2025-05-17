# This is the parent/base class
print(""""    
""")
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power} with strength level {self.strength}!")


    # This is a child class that inherits from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")


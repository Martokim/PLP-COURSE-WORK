from vehicles import Car, Plane

my_car = Car()
my_plane = Plane()

# Polymorphism in action
for vehicle in (my_car, my_plane):
    vehicle.move()

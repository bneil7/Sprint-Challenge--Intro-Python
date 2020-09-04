# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

### BASE CLASS ###
class Vehicle:
    pass


### child 1: ground ###
class GroundVehicle(Vehicle):
    pass


# ground child 1
class Car(GroundVehicle):
    pass


# ground child 2
class Motorcycle(GroundVehicle):
    pass


### child 2: flight ###
class FlightVehicle(Vehicle):
    pass


# flight child 1
class Starship(FlightVehicle):
    pass


# flight child 2
class Airplane(FlightVehicle):
    pass

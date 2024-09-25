# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    def __init__(self, reg_num, type, owner, owner_count):
        self.reg_number = reg_num
        self.type = type
        self.owner = owner
        self.transfer_count = owner_count
    def update_owner(self, new_owner):
        vehicle["Owner"] = new_owner
        return print_info()

# Task 2: Event Management System Enhancement

# - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
class VehicleSale:
    def __init__(self,name,date):
        self.name = name
        self.date = date
    def sell(self,name,date):
        print(f"{name} purchased the vehicle from {vehicle["Owner"]} on {date}!")
        vehicle["Owner Count"]+=1
        Vehicle.update_owner(vehicle,name)

def print_info():
    for key,value in vehicle.items():
        print(f"{key}:{value}")


vehicle = {"Registration Number":"1","Type":"SUV","Owner":"HN","Owner Count":1}

print_info()
VehicleSale.sell(vehicle,"Maggie","02/24/20")
VehicleSale.sell(vehicle,"Jerry","04/23/22")
VehicleSale.sell(vehicle,"Bert","09/24/24")

# - Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.




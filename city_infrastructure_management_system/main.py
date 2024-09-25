# Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_number = reg_num
        self.type = type
        self.owner = owner
    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle = Vehicle(1, 'SUV', 'HN')
print(vehicle.owner)
vehicle.update_owner('Maggie')
print(vehicle.owner)
vehicle.update_owner('Alfred')
print(vehicle.owner)
vehicle.update_owner('Gina')
print(vehicle.owner)


# Task 2: Event Management System Enhancement

# - Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

class Event:
    def __init__(self,name,date,count):
        self.name = name
        self.date = date
        self.count= count
    def add_participant(self,count):
        self.count += count
    def get_participant_count(self):
        return self.count
    
event = Event("HN's Birthday Bash","05/09/2025",0)
print(f"{event.name} will be held on {event.date}!")
event.add_participant(25)
event.add_participant(6)
rsvps = event.get_participant_count()
print(f"{rsvps} people will attend!")
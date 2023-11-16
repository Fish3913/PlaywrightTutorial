### Example one######
# class Vehicle:
#     def __init__(self,brand,doors,wheels):
#         self.brand=brand
#         self.doors=doors
#         self.wheels=wheels
#         print(f"I'm your new car, my name is {brand} and I have {doors} doors and {wheels}wheels")
#
# Veh=Vehicle("VW","4","all")
# Veh1=Vehicle("Ford","2","front ")

#### Example two#####
class Vehicle:
    def __init__(self, brand, doors, wheels):
        self.brand = brand     # initialize
        self.doors = doors
        self.wheels = wheels

    def car_greeting(self,local_slang):
        print(f"{local_slang}, I'm your new car, my name is {self.brand} and I have {self.doors} doors and {self.wheels} wheels")


veh = Vehicle("VW", "4", "all")
print(veh.wheels)
veh.car_greeting("yo")


# class Car:
#     brand='Volvo'
#
#
# car1=Car()
# print(car1.brand)
# car2=Car()
# print(car2.brand)

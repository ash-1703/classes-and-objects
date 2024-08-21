# """ 
# create a class Vehicle with max_speed and mileage instance attributes
# """

# class Vehicle:
#     def __init__(self,name,max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# # modelX = Vehicle(240,18)
# # print(modelX.max_speed, modelX.mileage)
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
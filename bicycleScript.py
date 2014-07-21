"""
Thinkful Python Unit 1 Lesson 6 Assignment 4
Implement Bicycle in Python using Classes

Qasim Ijaz
"""
import random
#import bicycle classes
from bicycle import *

#create 3 wheel types
road_wheel = Wheels(21, 70, "Road")
bmx_wheel = Wheels(18, 40, "BMX")
mountain_wheel = Wheels(24, 80, "Mountain")

#print(bmx_wheel.cost)

#create 3 frame types
aluminum_frame = Frames("Aluminum", 1000, 150)
carbon_frame = Frames("Carbon", 700, 130)
steel_frame = Frames("Steel", 500, 100)
#print(steel_frame.material)

#create 2 bicycle manufacturers
jedi_bikes = Manufacturers("Jedi Bikes", 18)
yoda_bikes = Manufacturers("Yoda Bikes", 20)
#print(yoda_bikes.percent)
#create 3 bicycle models for each of 2 manufacturers:

#Jedi_Bikes
jedi_bikes.new_bicycle("Jedi Roadster", aluminum_frame, road_wheel)
jedi_bikes.new_bicycle("Jedi BMX", carbon_frame, bmx_wheel)
jedi_bikes.new_bicycle("Jedi Climber", steel_frame, mountain_wheel)

#Yoda Bikes
#gives error: AttributeError: 'Bicycles' object has no attribute 'frame'
yoda_bikes.new_bicycle("Yoda AM", aluminum_frame, mountain_wheel)
yoda_bikes.new_bicycle("Yoda SB", steel_frame, bmx_wheel)
yoda_bikes.new_bicycle("Yoda CR", carbon_frame, road_wheel)

#Add bikes to Shop inventory
#TypeError: 'Manufacturers' object does not support indexing

martys = Shops("Marty\'s", 20)
martys.add_inventory(jedi_bikes[0])
martys.add_inventory(jedi_bikes[1])
martys.add_inventory(jedi_bikes[2])
martys.add_inventory(yoda_bikes[0])
martys.add_inventory(yoda_bikes[1])
martys.add_inventory(yoda_bikes[2])



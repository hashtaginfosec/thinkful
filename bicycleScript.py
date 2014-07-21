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
aluminum_frame = Frames("Aluminum", 150, 1000)
carbon_frame = Frames("Carbon", 130, 700)
steel_frame = Frames("Steel", 110, 500)

# print(steel_frame.weight)

#create 2 bicycle manufacturers
jedi_bikes = Manufacturers("Jedi Bikes", 18)
yoda_bikes = Manufacturers("Yoda Bikes", 20)


#every thing works well so far but when next statement is run, I get an error:
#    self.weight = Frames.weight + Wheels.weight * 2  <<< Hitting bicycles class and calculating total weight 
#AttributeError: type object 'Frames' has no attribute 'weight'

jedi_roadster = Bicycles("Jedi Roadster", jedi_bikes, aluminum_frame, road_wheel)



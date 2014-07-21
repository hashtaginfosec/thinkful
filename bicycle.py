"""
Thinkful Python Unit 1 Lesson 6 Assignment 4
Implement Bicycle in Python using Classes

Qasim Ijaz
"""
import random

class Wheels(object):
    def __init__(self, weight, cost, model):
        self.weight = weight
        self.cost = cost
        self.model = model


class Frames(object):
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost


class Manufacturers(object):
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent


#This class will construct a bike
class Bicycles(object):
    def __init__(self, name, manufacturer, frame, wheel):

        self.weight = Frames.weight + Wheels.weight * 2
        self.cost = self.frame.cost + self.wheel.cost * 2
        self.name = name
        self.wheel = wheel
        self.frame = frame
        self.manufacturer = manufacturer


class Shops(object):
    def __init__(self, name, margin):
        self.inventory = []
        self.margin = margin
        self.name = name
        self.profit = 0  #we start with no profit

    #Now we create bikes for inventory that will be set by bicycleScript.py
    def add_inventory(self, bicycle):

        self.inventory.append(bicycle)



class Customers(object):
    def __init__(self, name, fund, bikes):
        self.name = name
        self.fund = fund
        self.bikes = []


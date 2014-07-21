"""
Thinkful Python Unit 1 Lesson 6 Assignment 4
Implement Bicycle in Python using Classes

Qasim Ijaz
"""
import random
#import bicycle classes
from bicycle import *

#create 3 wheel types
road_wheel = Wheels(21, 40, "Road")
bmx_wheel = Wheels(18, 50, "BMX")
mountain_wheel = Wheels(24, 60, "Mountain")

#print(bmx_wheel.cost)

#create 3 frame types
aluminum_frame = Frames("Aluminum", 150, 70)
carbon_frame = Frames("Carbon", 130, 60)
steel_frame = Frames("Steel", 50, 50)

# print(steel_frame.weight)

#create 2 bicycle manufacturers
jedi_bikes = Manufacturers("Jedi Bikes", 18)
yoda_bikes = Manufacturers("Yoda Bikes", 20)


#create 3 bicycle models for each of 2 manufacturers:
jedi_roadster = Bicycles("Jedi Roadster", jedi_bikes, aluminum_frame, road_wheel)
jedi_bmx = Bicycles("Jedi BMX", jedi_bikes, carbon_frame, bmx_wheel)
jedi_climber = Bicycles("Jedi Climber", jedi_bikes, steel_frame, mountain_wheel)
yoda_cr = Bicycles("Yoda CR", yoda_bikes, carbon_frame, road_wheel)
yoda_am = Bicycles("Yoda AM", yoda_bikes, aluminum_frame, mountain_wheel)
yoda_sb = Bicycles("Yoda SB", yoda_bikes, steel_frame, bmx_wheel)


#creat a shop "Marty's" that takes 20% profit over wholesale cost
martys = Shops("Marty\'s Bicycle Shop", 20)
martys.add_inventory(jedi_roadster)
martys.add_inventory(jedi_bmx)
martys.add_inventory(jedi_climber)
martys.add_inventory(yoda_am)
martys.add_inventory(yoda_cr)
martys.add_inventory(yoda_sb)


#Try to add retail cost:
# for each_bike in martys.inventory:
#
#     if "Yoda" in each_bike.name:
#         print(each_bike.name + " >> " + str(each_bike.cost))
#         print(each_bike.name + " >> " + str(each_bike.cost))
#         print("Added Yoda Bike's margin of $" + str(yoda_bikes.percent) + " to " + each_bike.name)
#
#     elif "Jedi" in each_bike.name:
#         print(each_bike.name + " >> " + str(each_bike.cost))
#         each_bike.cost = each_bike.cost + jedi_bikes.percent + martys.margin
#         print("Added Jedi Bike's margin of $" + str(jedi_bikes.percent) + " to " + each_bike.name)





#create 3 customers with budges of 200, 500, and 1000
clients = {
    'Angel': Customers("Angel", 200),
    'Barb': Customers("Barb", 500),
    'Casey': Customers("Casey", 1000)
}

#Print name and total weight of each bike
print("-----------------------------------")
print(martys.name + " currently carries: ")
print("-----------------------------------")
for each_bike in martys.inventory:
    print(each_bike.name + " weighs " + str(each_bike.weight) + " and costs $" + str(each_bike.cost))
print("-----------------------------------")


#Print client name and budget amounts
for each_client in clients:
    budget_reach = []
    budget = clients[each_client].fund
    print("\n" + each_client + " has a budge of $" + str(budget) + " and they can afford following: ")
    for each_bike in martys.inventory:
        if each_bike.cost < budget:
            print(each_bike.name)
            budget_reach.append(each_bike.name)
print("-----------------------------------")
print("\n" + martys.name + " currently carries following bicycles: ")
for each_bike in martys.inventory:
    print(each_bike.name + " costs $" + str(each_bike.cost))

print("-----------------------------------")


#have each client buy one random bike
for each_client in clients:
    budget = clients[each_client].fund
    item = random.choice(martys.inventory)  # pick a random bike

    print(each_client + " would like to purchase " + item.name)

    if item in martys.inventory:
        if item.cost < budget:
            print("Wholesale cost is $" + str(Bicycles.wholesale_cost(item)))  # Still need to include retail cost
            #print(Shops.retail_cost(item, martys))

            martys.inventory.remove(item)  #bike has been purchased. Still need to add it to customer's inventory.

        else:
            print("Item not in your price range.")
    else:
        print("Item unavailable.")

    clients[each_client].fund = clients[each_client].fund - item.cost
    print(each_client + " has $" + str(clients[each_client].fund) + " left in their budget \n")


#print post-purchase inventory
print("-----------------------------------")
print("\n" + martys.name + " currently carries following bicycles: ")
for each_bike in martys.inventory:
    print(each_bike.name + " costs $" + str(each_bike.cost))

print("-----------------------------------")




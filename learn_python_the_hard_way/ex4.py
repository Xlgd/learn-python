cars = 100 # the amounts of the car 
space_in_a_car = 4 # the amounts of the space in a car
drivers = 30 # the amounts of the drivers
passengers = 90 # the amounts of the passengers
cars_not_driven = cars - drivers # the amounts of the cars that have no drivers
cars_driven = drivers # the amounts of the cars that have a driver
carpool_capacity = cars_driven * space_in_a_car # the amounts of space in cars that can use
average_passengers_per_car = passengers / cars_driven # the average passengers per car

# output the result
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

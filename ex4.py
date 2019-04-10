# Assign a value of 100 to cars  
cars = 100 
# Assign a value of 4 to space_in_a_car
space_in_a_car = 4 
# Assign a value of 30 to drivers
drivers = 30 
# Assign a value of 90 to passengers
passengers = 90
# Assign the  result of cars minus drivers to cars_not_driven
cars_not_driven = cars - drivers
# Assign the value of drivers to cars_driven
cars_driven = drivers 
# Assign the result of cars_driven multiplied by space_in_a_car to carpool_capactiy 
carpool_capacity = cars_driven * space_in_a_car
# Assign the result of passengers divided by cars_driven to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# Number of available cars 
print("There are", cars, "cars available.")
# Number of available drivers 
print("There are only", drivers, "drivers available.")
# The number of empty cars that there will be today
print("There will be", cars_not_driven, "empty cars today.")
# The number of people that we can transport today
print("We can transport", carpool_capacity, "people today.")
# The number of passengers to carpool today
print("We have", passengers, "to carpool today.")
# The number of passengers per car 
print("We need to put about", average_passengers_per_car, "in each car.")

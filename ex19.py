# create a function named chees_and_crackers with two arguments. 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print the amount of cheeses. 
    print(f"You have {cheese_count} cheeses!")
# print the number of boxes of crackers.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
# print "Man that's enough for a party!".
    print("Man that's enough for a party!")
# print "Get a blanket." and add a new line. 
    print("Get a blanket. \n")

# give the function values for the two arguments.
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# give amount_of_cheese and amount_of_crackers values 
print("OR, we can use variable from our script:")
amount_of_cheese = 10 
amount_of_crackers = 50 

# create a variable called cheese_and_crackers which is equal to amount_of_cheese and amount_of_crackres.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Do some math inside cheese_and_crackers. 
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Do math with both variables and numbers. 
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



name = ' Zed A. Shaw'
age = 35 # not a lie 
height = 74 # inches 
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White' 
hair = 'Brown' 

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actualy that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


# Convert inches and pounds to centimeters and kilograms

height_in_centimeters = height * 2.54
weight_in_kilograms = weight / 2.20465

print(f"The height in centimeters is {round(height_in_centimeters)} centimeters")
print(f"The weight in kilograms is {round(weight_in_kilograms)} kilograms")


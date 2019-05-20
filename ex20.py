# import argv from sys. 
from sys import argv

# set two arguments equal to argv. 
script, input_file = argv

# define print_all. 
def print_all(f):
    print(f.read())
# define rewind.
def rewind(f):
    f.seek(0)
# define print_a_line.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# set the value of current_file to open(input_file)
current_file = open(input_file)

# Print " First let's print the whole file" and add a new line. 
print("First let's print the whole file:\n")

# Pass current_file to print_all 
print_all(current_file)

# Print "Now let's rewind, kind of like a tape.")
print("Now let's rewind, kind of like a tape.")

# set the value of rewind to current_file 
rewind(current_file)

# print " let's print three lines:". 
print("Let's print three lines:")

# set the valu eof current_line to 1
current_line = 1 

# Pass current_line and current file to print_a_line. 
print_a_line(current_line, current_file)                    # current_line is equal to 1.  

# set the value of current_line to current_line + 1 
current_line = current_line + 1 

#Pass current_line and current file to print_a_line. 
print_a_line(current_line, current_file)                   # current_line is equal to 2. 

# set the value of current_line to curren_line + 1 
current_line= current_line + 1 

# Pass current_line and current_file to print_a_line. 
print_a_line(current_line, current_file)                  # current_line is equal to 3. 



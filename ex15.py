# import argv from sys.
from sys import argv

# set argv to take two inputs, script and filename.
script, filename = argv

# set the value of txt by opening a file. 
txt = open(filename)

# print the name of the file. 
print(f"Here's your file {filename}:")
# Read and print the contents of txt.
print(txt.read())

# print the string "Type the filename again:"
print("Type the filename again:")
# set the value of file_again to user input. 
file_again = input("> ")
# set the value of txt_again to file_again.
txt_again = open(file_again)

# Read and print the contents of the specified file..
print(txt_again.read())

# close the opened files.
txt.close()
txt_again.close()

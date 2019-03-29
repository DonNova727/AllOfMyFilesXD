#This used to import an argument into the code
from sys import argv
#This is used in order to inout a file for the code
script, input_file = argv
#This code allows the code to understand that in the following lins (f) is used for print_all
def print_all(f):
#Thia line is used in order to tell the compter to read and print what is being read
   print(f.read())
#In this line the code once again setting a variable for (f) to be rewind.
def rewind(f):
#In this line the variable for rewind causes the code to be read in reverse
     f.seek(0)

#This lets the code know to print out the lines count or the number of lines used in the print codes
def print_a_line(line_count, f):
     print(line_count, f.readline())

#This tells the code that when current_file is used it should open the file imputed by the coder
current_file = open(input_file)

print("First let's print the whole file:\n")
#This tells the code to print everything in the given file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
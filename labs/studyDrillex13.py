# In this line thae arguments are being imported into the code
from sys import argv
#the variables are being used with the argument
script, first, second, third = argv

#the code is using the argument in order to write the code through the bash interperter instead of running the file
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


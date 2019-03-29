#First Def means Define in the first Line it's defining print_two to work with the arguments
#this line similar to a regualr script with arguments where it's just using two arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#Second This line does something similar to the first except with print_two again the code dosen't need to unpack the arguments it allows us to write code irectly into the parenthesis
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
#Third
def print_one(arg1):
    print(f"arg1: {arg1}")
#Fourth
def print_none():
    print("I got nothin'.")

#These lines use the defined arguments to write code in the bash consol when ran such as my name appearing as argument 1 and 2 in the beggining
print_two("Donovan","Coleman")
print_two_again("Donovan","Coleman")
print_one("First!")
print_none()

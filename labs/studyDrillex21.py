#In this line the command "def" along with add lets python know to use add as +
def add(a , b):
    print(f"ADDING {a} + {b}")
# in tis line the code is  taking the two added variables a and b have them be returned or shown to the user when in the bash as the a+b
    return a + b
#In this line the command "def" along with subtract lets python know to use subtract as -
def subtract(a , b):
    print(f"SUBTRACTING {a} - {b}")
# in this line the code is returning the vaable a and b but with the subtraction symbol
    return a - b
#In this line the command "def" along with multiply lets python know to use multiply as *
def multiply(a , b):
    print(f"MULTIPLYING {a} * {b}")
#This line let's the vaiable a and b come back into the bash consol before multiplication as (a * b)
    return a * b
#In this line the command "def" along with divide lets python know to use divide as /
def divide(a ,b):
    print (f"DIVIDING {a} / {b} ")
#In this line the code uses the information above in order to show in the bash what two number are about to be divided
    return a / b


print(" Let's do some math with only functions!")
#The following lines uses the defined information above to do math equations with only the use of functions
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
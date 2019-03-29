#In this line thae arguments are being imported into the code
from sys import argv
#the variables are being used with the argument
script, user_name  = argv
prompt = '> '
#In these lines the questions are being asked and the input is being saved everytime they're answered
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
#This line uses all of the previous information from the questions in order to fill the variables and create dialouge
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
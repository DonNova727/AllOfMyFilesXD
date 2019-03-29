#In line the values of cheese and crackers are being put directly into their respective variables

#These lines take the variables and uses def to define the variables given in the code allowing cheese to gain the value 20 and crackers 30
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for the party!")
    print("get a blanket.\n")
print("We can just give the function numbers directly:")
cheese_and_crackers(20 , 30)
#This line uses the basic way of creating variables by using the = sign to assign a variable to a certain value
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#In this line the values of cheese_and_crackers is done in math to get the value but in order to have an output of two numbers is seperated by the comma
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

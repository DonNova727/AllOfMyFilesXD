the_count = [1,2,3,4]
fruits = ['apples', 'oranges', 'pears','apricots']
change=[1,'pennies', 2, 'dimes', 3, 'quarters']

#These kinds of loop goes through the entire list based off of the order given in the first line
for number in the_count:
    print(f"This is count {number}.")

#This method is the same as the one above
for fruits in fruits:
    print(f"A fruit of type: {fruits}")
    
#We can also get mixed versions of or list
#We use the {} so we don't know whats inside
for i in change:
    print(f"I got {i}")
    

elements = []
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #appen is a funcion that lists 
    elements.append(i)
    


#We are now capable of printing th einformation do to what is shown above
for i in elements:
    print(f"Element was: {i}")
    
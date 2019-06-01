#Adds states to the list
states = {
    'Oregon' : 'OR' ,
    'Flordia': 'FL' ,
    'California':'CA',
    'New York':'NY',
    'Michigan': 'MI',
    }
    
#Adds cities to the list    
cities = {
    'CA':'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'PortLand'

#Prints cities
print('-' * 10)
print("NY  State has:", cities['NY'])
print("OR State has : ",cities['OR'])
#prints states
print('-' * 10)
print("Michigan's abbreviation is: " , states['Michigan'])
print("Flordia's abreviation is :" , states['Flordia'])


print('-' * 10)
print("Michigan has : ", cities[states['Michigan']])
print("Flordia has: " , cities[states['Flordia']])

print('-' * 10)
for state , abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-'* 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city} ")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state}state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
#carefullly aquires state that may not be there    
print('-' * 10)

# Create a mapping of state to abbreviation
states = {'Oregon': 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#after printing the dictionary, i see dictionary is not ordered
print cities

#figured i could create an empty dictionary and add things to it using
#square brackets.
birds = {}
birds['bird1'] = 'Eagle'
birds['bird2'] = 'Swallow'
birds['bird3'] = 'Kite'
birds['bird4'] = 'Robbin'
print birds # After printing this i see this is not ordered either.

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is:  ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items(): #You need to call .items to see each value for each key.
    print "%s state is abbreviated %s" % (state, abbrev)

#print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now both at the same time.
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s", (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

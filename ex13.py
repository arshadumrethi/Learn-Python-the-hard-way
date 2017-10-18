from sys import argv

script, first, second, third , four = argv


print "The script is called", script

##Included version with raw_input, uncomment to test it.

first = raw_input("What do you want to call the first variable?" )
print "Your first variable is called", first

#second = raw_input("What do you want to call the second variable?" )
print " Your second variable is:", second

#third = raw_input("Do you like coffee?" )
print "Your thoughts about coffee ", third

#four = raw_input("What is gogo ram's last name? ")
print "Gogo ram", four

##Code example with raw_input passed to argv
# script, weather, feeling = argv
#
# print "Hot or Cold",
# weather = raw_input()
#
# print "Happy or sad",
# feeling = raw_input()
#
# print "The name of the script is:" , script
# print "The day is:", weather
# print "Today I am feeling:", feeling

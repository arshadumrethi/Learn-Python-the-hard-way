#Initial Strings are assigned
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #S inside S

#Variables are called to print
print x
print y

#Variable containing string called inside of another string
print "I said: %r" % x #S inside S
print "I also said: '%r'." % y #String inside String

#Variable hilarious is set to a bool - False and then called inside a string.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#print type(hilarious) Use this to check type of Variable

print joke_evaluation, hilarious

w = "This is the left side of..."
e = "a string with a right side."

# It is possible to add two strings together but not a string and integer
print w + e

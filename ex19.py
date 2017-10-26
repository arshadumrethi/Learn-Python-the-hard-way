# Making the function cheese and crackers : It takes two arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses" % cheese_count
    print "You have %d boxes of crackers!"  % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# Here we pass two numbers as arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Here we set variables equal to two numbers.
print "OR , we can use variable from our script:"
amt_of_cheese = 10
amt_of_crackers = 50

# We now pass those variables as arguments
cheese_and_crackers(amt_of_cheese, amt_of_crackers)

# We pass math into the two arguments.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# We add math to the variables and add them as arguments.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amt_of_cheese + 10, amt_of_crackers + 20)

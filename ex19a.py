# Defining the triple function.
def triple(x):
    print x**3

triple(9)

# Defining the multiply function.
def multiply(x, y):
    print x*y

#Using two numbers as arguments for multiply.
multiply(2, 4)

#Setting some Variables
myvar = 240
avar = 10

#Using two Variables as arguments.
multiply(myvar, avar)

# Using math and Variable as arguments.
multiply(myvar*2, avar)

#Using raw input as arguments. Remember to use Int to convert raw_input from str
print "Enter 1st number"
mynum = int(raw_input())

print "Enter 2nd number"
yournum = int(raw_input())

multiply(mynum, yournum)

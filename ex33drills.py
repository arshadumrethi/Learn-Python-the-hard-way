#Study drill number 1. Remember to comment out study drill 2 before running.
i = 0
numbers = []
var = int(raw_input())

def counter(var):
    i = 0
    numbers = []
    while i < var:
        print "Top number is %d" % i
        numbers.append(i)

        i += 1
        print "Bottom number is %d" % i

    for num in numbers:
        print num

counter(var)

#Study drill number 2. Remember to comment out study drill 1 before running.
i = 0
numbers = []

var = int(raw_input("Enter your number" ))
n = int(raw_input("Increase by:" ))

def counter(var, n):
    i = 0
    numbers = []
    while i < var:
        print "Top number is %d" % i
        numbers.append(i)

        i += n
        print "Bottom number is %d" % i

    for num in numbers:
        print num

counter(var, n)

#Study drill number 3: Get rid of the while loop and use for loop and range.
i = 0
numbers = []
var = int(raw_input())

def counter(var):
    i = 0
    numbers = []
    for i in range(var):
        print "Top number is %d" % i
        numbers.append(i)
        print "Bottom number is %d" % i

    for num in numbers:
        print num

counter(var)

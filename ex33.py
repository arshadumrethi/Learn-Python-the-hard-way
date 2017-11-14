i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

#My own cleaner version of the above code.
# i = 0
# numbers = []
#
# while i < 6:
#     #print "Top number is %d" % i
#     numbers.append(i)
#
#     i += 1
#     #print "Bottom number is %d" % i
#
# for num in numbers:
#     print num

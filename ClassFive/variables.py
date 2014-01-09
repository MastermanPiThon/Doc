#Variables

a = 6
b = 7
c = a * b

print "Answer: {}.  Question: What is the result of {} times {}?".format (c, a, b)


d = "Some text"

print d

list0 = [a, b, c, d]

list1 = list0[:]

list1[0] = "Six"

list2 = list0[2:4]

list2.append ("Banana")

print "First Array", list0

print "Second Array", list1

print "Third Array", list2


table0 = {"one": 1, "two" : 2, "three" : 3}

print table0

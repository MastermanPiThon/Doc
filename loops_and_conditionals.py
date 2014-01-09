#Loops and Conditionals

if 5 < 6:
    print "Obviously yes"
elif 3 < 4:
    print "Actually no"
else:
    print "Obviously not"

a = 0
while a < 100:
    val = raw_input("Enter a number less than 100: ")
    try:
        a = int(val)
    except:
        a = 0
    if a == 42:
        print "The Answer"

    if a != 42:
        print "Not the Answer"



while True: 
    val = raw_input ("Enter a number between 1 and 2: ")
    try:
        a = float (val)
    except:
        print "not a number"

    if a > 1 and a < 2:
        break

table0 = {"one": 1, "two" : 2, "three" : 3}
for text, number in table0.items():
    print "{0:5} {1:5}".format (text, number)


# Reading and writing files

# r: open for read
# w: open for write (erases existing file
# r+: open for read and write
# a: open file for write data to the end of an existing file

#Read

#The Unsafe way.  Must remember to close.
f = open ("topics.txt", "r")

for line in f:
    print line

f.seek (0)

print f.read ()

f.close ()

#The safe way.  Automatically closed
with open ("topics.txt", "r") as f:
    for line in f:
        print line

#Write

with open ("test.txt", "w") as f:
    f.write ("Something")

with open ("test.txt", "r+") as f:
    print f.read ()
    f.write ("End")
    f.seek (0)
    f.write ("Start") 
    f.seek (0)
    print f.read ()


# Read/Write JSON
import json

a = ["one", 3, "banana"]

with open ("test.txt", "w") as f:
    json.dump (a, f)


with open ("test.txt", "r") as f:
    b = json.load (f)

print a
print b


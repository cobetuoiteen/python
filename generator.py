import pdb

def gen():
    print ("in gen")
    x, y = 1, 2
    yield x, y
    x += 1
    yield x, y
    y += 1
    yield x, y
    print ("out gen")



it = gen()

print (it.next())
print (it.next())
print (it.next())

try:
    print (it.next())
except StopIteration:
    print ("Iteration finished")

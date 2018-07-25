import pdb

class seq:
    def __init__(self):
        print ("I am in init")
        self.x = 0

    def next(self):
        print ("I am in next")
        self.x += 1
        return self.x

    def __iter__(self):
        print ("I am in iter")
        return self

s = seq()
n = 0

print ("in loop")
for i in s:
    print (i)
    n += 1
    if n > 10:
        break

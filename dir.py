import sys
 
class Object:
   def __init__(self):
      pass
   def examine(self):
      print (self)
 
 
o = Object()

print ("******************") 
print ("dir(o)")
print (dir(o))

print ("******************")
print ("dir([])")
print (dir([]))

print ("******************")
print ("dir({})")
print (dir({}))

print ("******************")
print ("dir(1)")
print (dir(1))

print ("******************")
print ("dir()")
print (dir())

print ("******************")
print ("dir(len)")
print (dir(len))

print ("******************")
print ("dir(sys)")
print (dir(sys))

print ("******************")
print ("dir(\"String\")")
print (dir("String"))
print ("******************")

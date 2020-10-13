#Defines the function
def cross_bridge (steps):
  for steps in range(0,steps,1) :
    print ("Crossed step!")
  if (steps < 5):
    print ("We have to keep going,the bridge is collapsing!\n")
  elif (steps <= 5):
    print ("We made it across!")

#Calls the function with an optional argument
cross_bridge(5)


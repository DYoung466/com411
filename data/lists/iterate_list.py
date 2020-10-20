def directions():
  directions = ["Move Forwards","Move Backwards","Turn Left","Turn Right "]
  return directions 

def menu ():
  print ("Please choose a direction ")
  directions_var = directions()
  for index in range(0,len(directions_var),1):
    print("{} : {}".format (index+1,directions_var[index]))


menu()
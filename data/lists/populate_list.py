def directions():
  directions = ["Move Forwards","Move Backwards","Turn Left","Turn Right "]
  return directions 

def menu ():
  print ("Please choose a direction ")
  directions_var = directions()
  for index in range(0,len(directions_var),1):
    print("{} : {}".format (index,directions_var[index]))
    

def run():
  route = []
  directions_var = directions()
  print("Working out escape route")
  for index in range (0,3,1):
    menu_var = menu()
    route.append(input("Choose a direction "))
  route_var = route
  print (directions_var[route_var])

  
  
 

run()
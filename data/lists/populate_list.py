def directions():
  directions = ["Move Forwards","Move Backwards","Turn Left","Turn Right "]
  return directions 

def menu ():
  print ("Please choose a direction ")
  directions_var = directions()
  for index in range(0,len(directions_var),1):
    print("{} : {}".format (index,directions_var[index]))
<<<<<<< HEAD
  direction_index  = int(input ("Choose a direction "))
  return directions_var[direction_index]
=======
    
>>>>>>> be64fcf0b05bd0fc91fad7b7358c3ef32aa8bb96

def run():
  route = []
  directions_var = directions()
  print("Working out escape route")
<<<<<<< HEAD
  for index in range (0,5,1):
    menu_var = menu()
    route.append(menu_var)
  print(route)
  
=======
  for index in range (0,3,1):
    menu_var = menu()
    route.append(input("Choose a direction "))
  route_var = route
  print (directions_var[route_var])
>>>>>>> be64fcf0b05bd0fc91fad7b7358c3ef32aa8bb96

  
  
 

run()
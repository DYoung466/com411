def directions():
  directions = ["Move Forwards","Move Backwards","Turn Left","Turn Right "]
  return directions 

def menu ():
  print ("Please choose a direction ")
  directions_var = directions()
  for index in range(0,len(directions_var),1):
    print("{} : {}".format (index,directions_var[index]))
  direction_index  = int(input ("Choose a direction "))
  return directions_var[direction_index]


def run():
  route = []
  directions_var = directions()
  print("Working out escape route")
  for index in range (0,5,1):
    menu_var = menu()
    route.append(menu_var)
  print(route)
  


  
  
 

run()
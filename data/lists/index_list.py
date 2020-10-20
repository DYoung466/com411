def movement ():
  path = ["Move Forward", "10", "Move Backward","5", "Move Left", "3","Move Right","1"]
  return path

def run ():
  print("Moving")
  path_var = movement()
  for element in range(0,(len(path_var)),2):
    print (path_var [element], "for ", end ='')
    element=element +1
    print (path_var[element])

run()
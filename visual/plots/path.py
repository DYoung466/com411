import matplotlib.pyplot as plt 

def coordinate():
  x = input("Please enter an  x value...")
  y = input("Please enter a y value...")
  return (x,y)

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for i in range (0,4,1):
    coord_call = coordinate()
    x_var = coord_call[0]
    y_var = coord_call[1]
    x_values.append(x_var)
    y_values.append(y_var)
  return [x_values, y_values]

def run():
  values = path()
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.plot(values[0],values[1])
  plt.show()

run()


 


import matplotlib.pyplot as plt 

def data():
  paths = {}
  line_type = input ("What type of line would you like? ")
  line_colour = input ("What colour line would you like? ")
  line_marker = input ("What marker would you like? ")
  paths["ltype"] = line_type
  paths["colour"] = line_colour
  paths["marker"] = line_marker
  return paths

def generate():
  x_list = [1,2,3]
  y_list = [1,2,3]
  line_amount = int (input("How many lines? "))
  for i in range(line_amount):
    data_var = data()
    print (data_var)
    data_combined = data_var["colour"]+data_var["marker"]+data_var["ltype"]
    print (data_combined)
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.plot(x_list, y_list, data_combined)
    plt.show()

def run():
  print("Running...")
  generate()
  print("Done")

run()

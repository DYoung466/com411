def combined():
  fig, axs = plt.subplots(1)
  x_green = [3,3,7,3]
  y_green = [3,5,4,3]
  x_red = [3,5,7,3]
  y_red = [3,5,3,3]
  x_blue = [3,5,7,3]
  y_blue = [5,3,5,5]
  x_yellow = [7,7,3,7]
  y_yellow = [3,5,4,3]
  plt.plot(x_green,y_green,"g*-.")
  plt.plot(x_red,y_red,"ro--")
  plt.plot(x_blue,y_blue,"bs:")
  plt.plot(x_yellow,y_yellow,"yp-")
  plt.show()
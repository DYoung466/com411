import matplotlib.pyplot as plt 
def small ():
  plt.xlabel("x values")
  plt.ylabel("y values")
  x_list_small = [3,4]
  y_list_small = [3,3]
  x_list_small_2 = [3,4]
  y_list_small_2 = [4,4]
  x_list_small_3 = [3,3]
  y_list_small_3 = [3,4]
  x_list_small_4 = [4,4]
  y_list_small_4 = [3,4]
  plt.plot(x_list_small, y_list_small,'ro--')
  plt.plot(x_list_small_2, y_list_small_2,'ro--')
  plt.plot(x_list_small_3, y_list_small_3,'ro--')
  plt.plot(x_list_small_4, y_list_small_4,'ro--')
  

def med ():
  x_list_med = [2,5]
  y_list_med = [2,2]
  x_list_med_2 = [2,5]
  y_list_med_2 = [5,5]
  x_list_med_3 = [2,2]
  y_list_med_3 = [2,5]
  x_list_med_4 = [5,5]
  y_list_med_4 = [2,5]
  plt.plot(x_list_med, y_list_med,'gs--')
  plt.plot(x_list_med_2, y_list_med_2,'gs--')
  plt.plot(x_list_med_3, y_list_med_3,'gs--')
  plt.plot(x_list_med_4, y_list_med_4,'gs--')
  

def large ():
  plt.xlabel("x values")
  plt.ylabel("y values")
  x_list_large = [1,6]
  y_list_large = [1,1]
  x_list_large_2 = [1,6]
  y_list_large_2 = [6,6]
  x_list_large_3 = [1,1]
  y_list_large_3 = [1,6]
  x_list_large_4 = [6,6]
  y_list_large_4 = [1,6]
  plt.plot(x_list_large, y_list_large,'b*-')
  plt.plot(x_list_large_2, y_list_large_2,'b*-')
  plt.plot(x_list_large_3, y_list_large_3,'b*-')
  plt.plot(x_list_large_4, y_list_large_4,'b*-')
  

def run():
  large()
  med()
  small()
  plt.show()

run()
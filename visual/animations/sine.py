import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
     
fig, ax = plt.subplots()
    
def animate(frame):    
  ax.cla()
  ax.set_xlim(0,360)
  ax.set_ylim(-2,2)
  ax.tick_params(which='major', length = 8)
  PI = np.pi
  x_values = np.arange(0, frame)
  x_rad = ((x_values * (PI/180)+ frame / 50))
  y = np.sin(x_rad)
  ax.plot(x_values,y,'b')

     
def run():
  global fig  
  simple_animation = animation.FuncAnimation(fig,animate,frames =720, interval = 1)
  plt.show()
      
run()  
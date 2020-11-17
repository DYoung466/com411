import matplotlib.pyplot as plt
fig, axs = plt.subplots(1,2, sharex='all', sharey ='all')
 



def read_data (file_path):
  with open (file_path) as file:
    temps_list = []
    for line in file:
      line_strip = int( line.strip("\n"))
      temps_list.append(line_strip)
  print(temps_list)
  return temps_list

def run():
  file_input = input("Where is the file located? ")
  var_list = read_data(file_input)
  print (var_list)
  x = range(0,7,1)
  y = var_list
  axs[0].plot(x, y)
  axs[0].set_xlabel('Days')
  axs[0].set_xlim(0, 7)
  axs[0].set_ylabel('Temps')
  axs[0].set_ylim(0, 30)
  axs[1].plot(x, y)
  axs[1].set_xlabel('Days')
  axs[1].set_xlim(0, 7)
  axs[1].set_ylabel('Temps')
  axs[1].set_ylim(0, 30)
  

  plt.show()



  

run()

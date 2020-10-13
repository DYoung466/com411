#Defines multiple functions
def display_ladder (steps):
  for steps in range (0,steps,1):
    print ("| |\n***\n| |")

def create_ladder():
  steps = int(input ("How many steps are  there? "))
  display_ladder(steps)

create_ladder()
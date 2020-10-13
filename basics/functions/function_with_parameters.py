#Defines  the function with multiple parameters
def climb_ladder (steps_remaining,steps_passed):
  if (steps_remaining > steps_passed):
    print("We still have a way to go!\nKeep going!")
  elif (steps_remaining == steps_passed):
    print("We are halfway there!\nKeep going!")
  elif (steps_remaining < steps_passed ) and (steps_remaining != 0):
    print ("We are almost there!")
  elif (steps_remaining == 0)  and (steps_passed > 0):
    print("We made it!")
  else:
    print("Oh no we haven't had the correct input\nPlease restart!")

#Call the function with arguments to test each case       

climb_ladder (4,2)
climb_ladder (4,4)
climb_ladder (2,4)
climb_ladder (0,5)


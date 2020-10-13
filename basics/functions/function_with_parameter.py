#Defines the function
def escape_by(plan):
  if (plan == "jumping_over"):
    print ("We cannot escape by jumping over \nIt's too big!")
  elif (plan == "running_around"):
    print ("We cannot escape by running around it \nIt's too wide!")
  elif (plan == ("going_deeper")):
    print ("We can escape by running away\nThat's our only option!\nWe need to go deeper!")
  else:
    print("Oh no!\nPlease restart the program!")
  return plan
escape_by("jumping_over")
escape_by("running_around")
escape_by("going_deeper")
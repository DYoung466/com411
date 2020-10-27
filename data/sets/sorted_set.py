def observed ():
  observations =[]
  for index in range (0,5,1):
    observations.append(input("Please enter what you see "))
  return observations

def remove_observations (observations):
  observations_var = observations
  print(observations_var)
  remove_var =input("Do you wish to remove an observation? ")
  while (remove_var != "No"):
    remove_input =input("What would you like to remove: ")
    observations_var.remove(remove_input)
    remove_var =input("Do you wish to remove an observation? ")

def run():
  observations_var=observed()
  remove_observations(observations_var)
  print(observations_var)
  print("")
  observations_set = set()
  for observations in observations_var:
    observations_set.add((observations, observations_var.count(observations)))
    print("Observed",observations,observations_var.count(observations),"times")
  for key, value in observations_set:
    print (f"{key} observed {value} times.")


run()
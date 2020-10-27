def observed ():
  observations =[]
  for index in range (0,7,1):
    observations.append(input("Please enter what you see "))
  return observations

def run():
  print ("Couting observations...")
  observations_list = observed()
  observations_set = set()
  for observations in observations_list:
    observations_set.add((observations, observations_list.count(observations)))
  print(observations_set)

run()


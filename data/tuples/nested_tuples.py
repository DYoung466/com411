def steps ():
  likelihoods = []
  likelihoods.append (("Step 1", 50))
  likelihoods.append (("Step 2", 38))
  likelihoods.append (("Step 3", 27))
  likelihoods.append (("Step 4", 99))
  likelihoods.append (("Step 5", 4))
  return likelihoods

def run():
  steps()
  likelihoods_var = steps()
  good_steps = []
  bad_steps = []

  for likelihood in likelihoods_var:
    if (likelihoods_var[1] >= 50):
      bad_steps.append (likelihood)
    else:
      good_steps.append (likelihood)
      
  print ("There are ",len(good_steps), "good steps")
  print ("There are ",len(bad_steps), "bad steps")

run()

def likelihood ():
  likelihoods = [50,38,27,99,4]
  return min(likelihoods)

def run():
  likelihoods_var = likelihood()
  print ("The minimum likelihood of failing: {}%".format(likelihoods_var))

run()

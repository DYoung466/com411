def likelihood():
  likelihoods = [50,38,27,99,4]
  return min(likelihoods),max(likelihoods)

def run():
  likelihood_var =likelihood()
  print ("The minimum likelihood of falling is {}%".format(likelihood_var[0]))
  print ("The maximum likelihood of falling is {}%".format(likelihood_var[1]))

run()

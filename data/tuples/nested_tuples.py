def steps ():
  likelihoods = []
  likelihoods.append ("Step1",50)
  likelihoods.append ("Step2",38)
  likelihoods.append ("Step3",27)
  likelihoods.append ("Step4",99)
  likelihoods.append ("Step5",4)
  print (likelihoods)
  return likelihoods

  def run():
    likelihoods_var = steps()
    good_steps = []
    bad_steps = []
    for element in range (0,len(likelihoods_var),2):
      if (likelihoods_var[element] >= 50):
        bad_steps.append (1)
      elif (likelihoods_var[element] < 50):
        good_steps.append (1)
      
    print ("There are ",good_steps)
    print ("There are ",bad_steps)

  steps()

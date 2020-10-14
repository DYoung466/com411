#Defines the functions:

def sum_weights(beep_weight,bop_weight):
  total_weight = (( beep_weight + bop_weight))
<<<<<<< HEAD
  return  total_weight

def calc_avg_weights (beep_weight,bop_weight):
  avg_weight = float(((beep_weight+bop_weight)/2))
=======
  return  (total_weight)

def calc_avg_weights (beep_weight,bop_weight):
  avg_weight = float((sum_weights/2))
>>>>>>> 2fa3116b812f462c979f22a6516637b63fa5399e
  return float( avg_weight)

def run ():
  user_choice = input ("Sum or average? ")
  if (user_choice == "sum") :
    print("Sum!")
    print("")
<<<<<<< HEAD
    beep_weight = int(input ("Please enter Beep's weight "))
    bop_weight = int(input ("Please enter Bop's weight "))
=======
    beep_weight = input ("Please enter Beep's weight ")
    bop_weight = input ("Please enter Bop's weight ")
>>>>>>> 2fa3116b812f462c979f22a6516637b63fa5399e
    totalSum = sum_weights(beep_weight,bop_weight)
    print(totalSum)
  
  elif (user_choice == "average"):
    print("average")
    print("")
    beep_weight = float(input ("Please enter Beep's weight "))
    bop_weight = float(input ("Please enter Bop's weight "))
    totalAvg = calc_avg_weights (beep_weight,bop_weight)
    print (totalAvg)


run()


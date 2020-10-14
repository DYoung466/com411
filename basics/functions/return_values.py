#Defines the functions:

def sum_weights(beep_weight,bop_weight):
  total_weight = (( beep_weight + bop_weight))
  return  total_weight

def calc_avg_weights (beep_weight,bop_weight):
  avg_weight = float(((beep_weight+bop_weight)/2))
  return float( avg_weight)

def run ():
  user_choice = input ("Sum or average? ")
  if (user_choice == "sum") :
    print("Sum!")
    print("")
    beep_weight = int(input ("Please enter Beep's weight "))
    bop_weight = int(input ("Please enter Bop's weight "))
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


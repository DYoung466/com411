#Defines the functions:

def sum_weights(beep_weight,bop_weight):
  total_weight = float(( beep_weight + bop_weight))
  return total_weight

def calc_avg_weights (beep_weight_bop_weight):
  avg_weight = float((sum_weights/2))
  return avg_weight

def run ():
  user_choice = input ("Sum or average? ")
  if (user_choice == "sum") :
    print("Sum!")
    print("")
    beep_weight = input ("Please entert Beep's weight ")
    bop_weight = input ("Please entert Bop's weight ")
    sum_weights (beep_weight,bop_weight)
    print (sum_weights)
  elif (user_choice == "average"):
    print("average")
    print("")
    beep_weight = input ("Please entert Beep's weight ")
    bop_weight = input ("Please entert Bop's weight ")
    calc_avg_weights (beep_weight,bop_weight)
    print (calc_avg_weights)

run()


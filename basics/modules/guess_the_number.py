from random import randrange


def play_guess_the_number ():
  min_input = int (input ("Enter your minimum value (1 or above) \n"))
  max_input = int(input ("Enter your maximum value (2 or above)\n"))
  rand_var = (randrange(min_input,max_input,1))
  guess_var=1## 
  while (guess_var != rand_var) and (guess_var != 0):
    guess_var = int( input ("Guess a number!\n-Enter 0 to give up-\n"))
    if guess_var > rand_var :
      print ("Your guess was too big!")
      print("")
    elif (guess_var < rand_var) and (guess_var != 0) :
      print ("Your guess was too small!")
      print("")
    elif guess_var == rand_var :
      print ("Your guess was correct!\nWell done!")
      print("")

  print ("The number was {}".format(rand_var))
  print("Thanks for playing")

play_guess_the_number()

#Defines the functions needed for the program

def box_function ():
  word_var = input("Please enter your choice of word ")
  print ("Your word is {}".format(word_var))
  print(("#"*((len(word_var))+4)))
  print ("#",word_var,"#")
  print(("#"*((len(word_var))+4)))
  return word_var

box_function()

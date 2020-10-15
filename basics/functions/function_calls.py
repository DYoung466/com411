#Defines the functions needed for the program

def box_function ():
  word_var = input("Please enter your choice of word ")
  print ("Your word is {}".format(word_var))
  print(("#"*((len(word_var))+4)))
  print ("#",word_var,"#")
  print(("#"*((len(word_var))+4)))
  return word_var

<<<<<<< HEAD
##To obtain lowercase 32 must be added to the original ASCII value

def lower_case():
  word_var = input ("Please enter your word ")
  print ("Your word is {}".format(word_var))
  for element in word_var:
    element_ord = ord (element)
    element_ord = element_ord + 32
    element_chr= chr(element_ord)
    print (element_chr, end = '')
  print("")
  return word_var


def upper_case():
  word_var = input ("Please enter your word ")
  print ("Your word is {}".format(word_var))
  for element in word_var:
    element_ord = ord (element)
    element_ord = element_ord - 32
    element_chr= chr(element_ord)
    print (element_chr, end = '')
  print("")
  return word_var

upper_case()
=======
box_function()
>>>>>>> 412527869c4269610c44093074d6a8ea98b34b26

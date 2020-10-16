#Defines the functions needed for the program

def box_function (word):
  print ("Your word is {}".format(word))
  print(("#"*((len(word))+4)))
  print ("#",word,"#")
  print(("#"*((len(word))+4)))
<<<<<<< HEAD
  print("")

##To obtain lowercase 32 must be added to the original ASCII value
##After watching the rest of the seminar, it is obvious that i could have made the upper and lower functions a lot smaller.#
##I have left these previous functions here but they are not called
=======

##To obtain lowercase 32 must be added to the original ASCII value
##After watching the rest of the seminar, it is obvious that i could have made the upper and lower functions a lot smaller.
>>>>>>> 39dbe785fa80e1d64a8f24075caa97fecef01efe

def lower_case(word):
  print ("Your word is {}".format(word))
  for element in word:
    element_ord = ord (element)
    element_ord = element_ord + 32
    element_chr= chr(element_ord)
    print (element_chr, end = '')
  print("")

def upper_case(word):
  print ("Your word is {}".format(word))
  for element in word:
    element_ord = ord (element)
    element_ord = element_ord - 32
    element_chr= chr(element_ord)
    print (element_chr, end = '')
  print("")

<<<<<<< HEAD
def new_lower_case(word):
  print(word.lower())
  return ("")

def new_upper_case(word):
  print(word.upper())
  return ("")


=======
>>>>>>> 39dbe785fa80e1d64a8f24075caa97fecef01efe
def reverse(word):
  reverse_word = ''
  for index in (range (len(word)-1,-1,-1)):
    reverse_word += word [index] 
  print ("{} | {}".format(word, reverse_word))

<<<<<<< HEAD
##This function requires some work
def repeated(word):
  iterations = int( input( "How many times should the word be repeated"))
  print ("You want it to repeat {} times ".format (iterations))
  print("")
  for iteration in range (iterations):
    if (iteration % 2 == 0):
      print(new_lower_case(word))
    else:
      print (new_upper_case(word))
=======
def repeated(word):
  iterations = int( input( "How many times should the word be repeated"))
  print ("You want it to repeat {} times ".format (iterations))
  for iteration in range (iterations):
    if (iteration % 2 == 0):
      print (upper_case(word))
    else:
      print (lower_case(word))
>>>>>>> 39dbe785fa80e1d64a8f24075caa97fecef01efe

def run ():
  word = input ("Please enter your word ")
  print ("")
  select_var = 0
  while (select_var != 6):
<<<<<<< HEAD
    print ("\nFunctions: ")
    select_var = int (input ("1.Box\n2.Convert to Lower Case\n3.Convert to Upper Case\n4.Reverse\n5.Repeat\n6.Exit\nWhich function would you like to run?\n "))
=======
    print ("Functions: ")
    select_var = int (input ("1.Box\n2.Convert to Lower Case\n3.Convert to Upper Case\n4.Reverse\n5.Repeat\n6.Exit\nWhich function would you like to run? "))
>>>>>>> 39dbe785fa80e1d64a8f24075caa97fecef01efe
    if (select_var == 1):
      box_function(word)
    elif (select_var == 2):
      lower_case (word)
    elif (select_var == 3):
      upper_case (word)
    elif (select_var == 4):
      reverse (word)
    elif (select_var == 5):
      repeated (word)
<<<<<<< HEAD
    elif (select_var == 6):
      print("Exiting")
=======
>>>>>>> 39dbe785fa80e1d64a8f24075caa97fecef01efe
    else:
      print("Command not recognised")


  

run()

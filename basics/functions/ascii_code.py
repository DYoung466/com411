#Program that determines the ascii code for a character
print("Program started! ")
user_input = input ("Please enter a single standard character? ")
if (len(user_input) == 1):
  print ("Your input was ", user_input)
  print ("The ASCII code for ",user_input, " is", "{}".format(ord(user_input)))
else:
  print("Please restart and enter a single standard character")
  

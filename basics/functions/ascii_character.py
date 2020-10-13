#Code that determines the character from an ascii code      
print ("Program started!")
user_input = int (input ("Please enter your ASCII code\nThis should be between 32 and 126 "))
user_input = abs(user_input)
if (user_input in range (32,127,1)):
  print ("The character represented by ", user_input ," is {}".format (chr(user_input)))
else:
  print ("Please restart the progam and input a valid ASCII code")
print("Program ended!")

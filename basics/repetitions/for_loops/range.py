print ("Wow it sure is dark in here")
print("")
brightness = int(input("What brightness should we adjust to?\nPlease choose an even number "))
print("")
iterations = ( brightness + 1)
if (iterations % 2 != 0):
  for brightness in range (brightness+ 1):
    print ("-------------------------------------")
    print ("Beep's Brightness", "* "* brightness)
    print ("Bop's Brightness ", "* "* brightness)
    print ("-------------------------------------")
    print ("")
    brightness = ( brightness  + 1)
    
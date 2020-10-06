print ("Painting machine!")
direction = 1
while (direction != 0):
  print ("Directions : up, down, left, right (Type 0 to exit)")
  direction = input ("Please choose a direction to paint in! ")
  if (direction == "up") or (direction == "Up"):
    print ("I am painting upwards!")
    direction = input ("Please choose a direction to paint in! ")
  elif (direction == "Down") or (direction == "down"):
    print ("I am painting downwards!")
    direction = input ("Please choose a direction to paint in! ")
  elif (direction == "left") or (direction == "Left"):
    print ("I am painting to the left!")
    direction = input ("Please choose a direction to paint in! ")
  elif (direction == "right") or (direction == "Right"):
    print ("I am painting to the right!")
    direction = input ("Please choose a direction to paint in! ")
print ("Thank you for painting!") 

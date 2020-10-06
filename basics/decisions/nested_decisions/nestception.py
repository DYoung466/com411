print ("Where is my spare battery?")
print ("There are 3 rooms")
print ("I see a bedroom, a bathroom and a lab")
location = input ("Where should I look?\n In the ")
if (location == "bedroom") or (location == "Bedroom"):
  print ("I am looking in the bedroom")
  print ("")
  print ("I see a bed")
  bedroom = input ("Should I look under the bed\n Yes or No ")
  if (bedroom == "Yes") or (bedroom == "yes"):
    print ("I see some clothes on the bed")
    onBed = input ("Should I look under the bed? \n Yes or No ")
    if (onBed == "Yes") or (onBed == "yes"):
      print ("I see some mess but no battery")
      print ("It's not in the bedroom\nLeaving room")

    else:
      print (" It's not in there\nLeaving room")

  else:
    print ("It's not in the bedroom\nLeaving room")
elif (location == "bathroom") or (location =="Bathroom"):
  print ("I see a cabinet")
  bathroom = input ("Should I look inside the cabinet?\n Yes or No ")
  if (bathroom == "yes") or (bathroom == "Yes"):
    print ("I see a note saying check the lab")
    print ("Exiting room")
  else:
    print ("Exiting the bathroom")
else:
  print ("Checking the lab")
  print ("")
  print ("I see a briefcase ")
  lab=input ("Should I look inside the briefcase? \n Yes or No ")
  if (lab == "yes") or (lab =="Yes"):
    print ("You found the battery!")
  else:
    print ("you should have checked the case")
location = input ("Where should I look?\n In the ")
#rearange this as it does not loop back to the room section

print ("Hi, I'm Bleep")
EnergyVar = 0
nameVar = input ("What's your name? ")
print ("Hi,",nameVar)
print ("")
helpVar = input ("My energy levels are low, could you help? ")
if (helpVar == "Yes") or (helpVar == "Yeah") or (helpVar == "yes") or (helpVar == "yeah"):
  print ("Thanks")
else:
  print ("Oh well, thanks anyway")
print ("")
print ("Please solve these programming questions to build up my energy!")
print ("")
print ("Which of these shows the user text?")
print ("")
print ("A. print")
print ("B. Text")
print ("C. primt")
print ("D. beans")
A1Var = input ("Please type the letter of your answer  ")
if (A1Var == "A") or (A1Var == "a"):
  print ("Correct!") 
  EnergyVar = EnergyVar + 1
elif (A1Var =="print") or (A1Var =="Print"):
  print ("Correct, but please only enter the letter")
  EnergyVar =EnergyVar + 1
else:
  print ("Incorrect, the correct answer was A")
print ("Energy levels = ", EnergyVar * "♦")
print ("")
print ("Next question!")
print ("")
print ("Which of these is not a data type? ")
print ("")
print ("A. Integer")
print ("B. Beans")
print ("C. Float")
print ("D. String")
A2Var = input ("Please type the letter of your answer  ")
if (A2Var == "B") or (A1Var == "b"):
  print ("Correct!") 
  EnergyVar = EnergyVar + 1
elif (A2Var =="beans") or (A1Var =="Beans"):
  print ("Correct, but please only enter the letter")
  EnergyVar =EnergyVar + 1
else:
  print ("Incorrect, the correct answer was B")
print ("Energy levels = ", EnergyVar * "♦")


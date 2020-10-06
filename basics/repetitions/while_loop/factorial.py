print ("Factorial Calculator!")
numVar = int(input ("Please enter a whole number!") )
print ("Your number is ",numVar)
numIteration = 1
numEnd = (numVar + 1)
numStore = 1 
while (numIteration != numEnd) :
  numStore = numIteration*numStore  
  numIteration=numIteration+1
print (numStore)



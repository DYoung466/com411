print ("What's that?\n\nYou see a word backwards?\n\nI can help with that!")
word = input ("What word do you see?\n\nPlease enter it here: ")
print ("So you see ",word)
print("Flipping word",end ="")
print("")
for count in range (len(word) -1,-1,-1):
  print(word[count], end =""),
print ("\nDone!")
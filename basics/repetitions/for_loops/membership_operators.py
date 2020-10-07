print  ("What phrase do you see ")
user_input = input ("What phrase do you see? ")
print("")
reversed = ""
for letter in user_input:
  reversed = letter + reversed
print (reversed)
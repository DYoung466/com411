def pattern ():
  sequences = {}
  sequences["short sequence"] = 3 
  sequences["Medium Sequence"] = 2  
  sequences["Long Sequence"]= 1 
  return sequences
def run():
  pattern_var=pattern()
  print (pattern_var)

run()
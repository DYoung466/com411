def search (fileVar):
  print("Searching")
  with open("locations.txt") as fileVar:
    for line in fileVar:
      print (line[0])

def run():
  print ("Searching")
  search("locations.txt")

run()
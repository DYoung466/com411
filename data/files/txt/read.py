def search (filePath):
  with open(filePath) as fileVar:
    for lines in fileVar:
      print (lines)

def run():
  print ("Searching")
  search("data/files/txt/locations.txt")

run()
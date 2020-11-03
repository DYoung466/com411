def search (filePath):
  print ("Searching...")
  sections = []
  books = []
  with open(filePath) as fileVar:
    for lines in fileVar:
      if lines.startswith("Section"):
        splitVar = lines.split(",")
        sections.append(splitVar)
      else:
        books.append(lines)
    print (sections,books)
  return (sections,books)

def run():
  search("data/files/txt/books.txt")


        
run()

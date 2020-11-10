def search (filePath):
  print ("Searching...")
  sections = []
  books = []
  with open(filePath) as fileVar:
    for lines in fileVar:
      if lines.startswith("Section"):
        splitVar = lines.split(":")
        sections.append(splitVar[1].replace ('\n',""))
      else:
        books.append(lines)
    print (sections,books)
  print("Done")
  return (sections,books)
  
def save(fileName,data):
  print("Saving")
  with open (fileName,"w") as file:
    file.write("Sections: ")
    for section in data [0]:
      file.write (f"{section},")

    file.write("\nBooks ")
    for book in data [1]:
      file.write (f"{book},")
  print("Done")

  

def run():
  data = search("data/files/txt/books.txt")
  save ("data/files/txt/sections-books.txt",data)

run()


import os
def cwd():
  file = os.getcwd()
  print("The current working file is {}".format (file))
  for file in os.listdir(file):
    print (file)

def run():
  print("Processing...")
  cwd()

run()



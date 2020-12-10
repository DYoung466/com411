class robot:
  #class attribute
  MAX_ENERGY = 100
  
  def __init__(self):
    #instance attribute
    self.name = "robot"
    self.age = 0
    self.energy= 0
  
  def display(self):
    #method
    print(f"I am {self.name}")


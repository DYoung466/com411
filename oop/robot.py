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

  def __str__(self):
    return f"{self.name} is {self.age} years old"

  def __repr__(self):
    return f"robot(name={self.name}, age = {self.age})"
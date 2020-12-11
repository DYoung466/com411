class human:
  MAX_ENERGY = 100
  
  def __init__(self):
    self.name = "Human"
    self.age = 0
    self.energy= human.MAX_ENERGY
  
  def display(self):
    print(f"I am {self.name}")

  def __str__(self):
    return f"{self.name} is {self.age} years old"

  def __repr__(self):
    return f"human(name={self.name}, age = {self.age})"



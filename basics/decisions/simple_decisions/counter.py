print ("Number counter!")
num1 = int(input ("Please enter your first number "))
num2 = int(input("Please enter your second number"))
num3 = int(input("Please enter your third number"))
even = int  
odd = int 
even = 0
odd = 0
if (num1 % 2 == 0): #even case
  print ("your first number is even")
  even = even +1
elif (num2 % 2 == 0): #even case
  print ("your second number is even")
  even = even +1
elif (num3 % 2 == 0): #even case
  print ("your third number is even")
  even = even +1
odd = 3 - even
print ("You have ", even, " even numbers")
print ("You have ", odd, " odd numbers")

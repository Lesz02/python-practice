# Exercise : Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.
# If they are tall enough and have enough credits, print "Enjoy the ride!"
# Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
# Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
# Else, print a message saying they have not met either requirement.
# code below 
height = int(input("what is your height(cm)?"))
credits = int (input("how many credits do you have?"))
if height >= 137 and credits >= 10:
  print ("Enjoy the ride!")
elif height <= 137 and credits >= 10:
  print ("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print ("you don't have enough credits.")
else:
  print ("You have not met either requirement.")

# program that checks whether a pH level is basic, acidic, or neutral.
# If ph is greater than 7, output "Basic".
# If ph is less than 7, output "Acidic".
# Else, output "Neutral".
# code below 💖
ph= int(input("Enter a ph value (0-14):"))
if ph > 7:
  print ("Basic")
elif ph < 7:
  print ("Acidic")
else: 
  print ("Neutral")

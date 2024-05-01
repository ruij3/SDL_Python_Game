import random

# Define lists of catagory
our_class = ["Jun Xiong", "Cherry", "Basil", "Gerrard", "Danny", "Franstin", "Ruijia", "Shi Jie", "Issac Liou", "Issac Tan", "Janelle", "Jordan", "Jovan", "He Yu", "Ameya", "Re", "Jia Sheng", "Kong Huai", "Qing En", "Xavier", "Breavince"]

north_east_line = ["Punggol", "Sengkang", "Buangkok", "Hougang", "Kovan", "Serangoon", "Woodleigh", "Potong Pasir", "Boon Keng", "Farrer Park", "Little India", "Dhoby Ghaut", "Clarke Quay", "Chinatown", "Outram Park", "HarbourFront"]

jc_shortform = ["ASRJC", "ACJC", "CJC", "HCI", "TMJC", "MI", "NYJC", "NJC", "JPJC", "SAJC", "TJC", "VJC", "YIJC"]

# Start game
catagory = input("I am Akinator. I can guess what you are thinking. First, choose a catagory (25/13 students, north east line stations, JCs in SG): ")


# Catagory: 25/13 students
if catagory == "25/13 students":
  valid = False
  while not valid:
    user_input = input("\nWho are you thinking of? ")
    if user_input not in our_class:
      print("That is not a student in our class. Please enter a valid student.")
    else:
      valid = True
  print("\nNow let me guess who you are thinking of.")
  correct = False
  while not correct:
    guess = random.choice(our_class)
    print("\nAre you thinking of", guess, "?")
    answer = input("Yes or No? ")
    if answer == "Yes":
      print("\nYes! I guessed it!")
      correct = True
    else:
      print("\nHmm. Let me think again.")
      our_class.remove(guess)


# Catagory: north east line stations
if catagory == "north east line stations":
  valid = False
  while not valid:
    user_input = input("\nWhat are you thinking of? ")
    if user_input not in north_east_line:
      print("That is not a station in north east line. Please enter a valid station.")
    else:
      valid = True
  print("\nNow let me guess what you are thinking of.")
  correct = False
  while not correct:
    guess = random.choice(north_east_line)
    print("\nAre you thinking of", guess, "?")
    answer = input("Yes or No? ")
    if answer == "Yes":
      print("\nYes! I guessed it!")
      correct = True
    else:
      print("\nHmm. Let me think again.")
      north_east_line.remove(guess)


# Catagory: JCs in SG
if catagory == "JCs in SG":
  valid = False
  while not valid:
    user_input = input("\nWhat are you thinking of? (Pls enter the short form of the JCs) ")
    if user_input not in jc_shortform:
      print("That is not a JC in Singapore. Please enter a valid JC.")
    else:
      valid = True
  print("\nNow let me guess what you are thinking of.")
  correct = False
  while not correct:
    guess = random.choice(jc_shortform)
    print("\nAre you thinking of", guess, "?")
    answer = input("Yes or No? ")
    if answer == "Yes":
      print("\nYes! I guessed it!")
      correct = True
    else:
      print("\nHmm. Let me think again.")
      jc_shortform.remove(guess)

# End game
print("\nThank you for playing!")
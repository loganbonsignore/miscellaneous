#Welcome user to ageCalc
print("""


Hi, welcome to ageCalc.

Calculate your age in any year in the future (or past!).
_____________________________________________________________________

""")

#Ask user if they would you like to proceed
user_input = input("Would you like to proceed? (y/n) : ")
#If no, terminate program.
if user_input != "y":
  print("Sorry to see you go. Goodbye.")
  print("We have terminated the program.")
  exit()

#Get variables from user
name = input("What's your name? :")
age = input("How old are you today? :")
year = input("What year do you want to calculate your age in? (yyyy) : ")

#Calculate age
old_age = (int(year) - 2020) + int(age)
years_long = (int(year) - 2020)

#Return data to user 
if years_long > 0:  
  print(F"""
    
You will be {old_age} years old in the year {year}. Thats {years_long} years into the future!""")
elif years_long == 0:
  print(F"""
    
You entered the current year! Your age did not change.""")
else:
  print(F"""
    
You were {old_age} years old in the year {year}. That was {abs(years_long)} years ago!""")

#Ask user if they want to try again.
user_input = input("""
Would you like to go again? (y/n) :""")

if user_input == "n":
  #If no, terminate program.
  print(f"Thanks for playing {name}! Goodbye.")
  print("We have terminated the program.")
  exit()
else:
  #If yes, user enters new continuous loop which they will stay in for the rest of the program.
  while user_input == "y":
    #Ask for a new "year" value from user
    year = input("What year do you want to calculate your age in? (yyyy) :")
    #Calculate new age
    old_age = (int(year) - 2020) + int(age)
    years_long = (int(year) - 2020)
    #Return data to user
    if years_long > 0:  
      print(F"""
        
You will be {old_age} years old in the year {year}. Thats {years_long} years in the future.""")
    elif years_long == 0:
      print(F"""
        
You entered the current year! Your age did not change.""")
    else:
      print(F"""
        
You were {old_age} years old in the year {year}. That was {abs(years_long)} years ago!""")
    #Ask user if they want to try again
    user_input = input("""
Would you like to go again? (y/n) :""")
    #Terminate program if answer is no
    if user_input == "n":
      print(f"""
Thanks for playing {name}!
We've terminated the program.""")
      exit()

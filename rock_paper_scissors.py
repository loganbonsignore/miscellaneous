import random

#Welcome message
print("""
Welcome to Rock, Paper, Scissors!

First player to win 5 games wins!
""")
user_input = input("Are you ready to play? (y/n) :")

#define starter variables
options = ["r", "p", "s"]
wins = 0
losses = 0

while user_input == "y":
    #Get computer choice
    cc = random.choice(options)
    #Get user choice
    uc = input("""
Rock, paper, scissors, SHOOT!: (r/p/s) :""")

    #If same choice
    if cc == uc:
        if cc == "r":
            cc = "Rock"
            uc = "Rock"
        elif cc == "p":
            cc = "Paper"
            uc = "Paper"
        elif cc == "s":
            cc = "Scissors"
            uc = "Scissors"
        print(f"""
--------------------------
Computer Choice: {cc}     
User Choice: {uc}         
--------------------------
You tie.                  
--------------------------
Wins: {wins}              
Losses: {losses}          
--------------------------
""")
        #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #computer:rock / user:paper
    elif cc == "r" and uc == "p":
        print(f"""
--------------------------
Computer Choice: Rock
User Choice: Paper
--------------------------
You win!
--------------------------
Wins: {wins + 1}
Losses: {losses}
--------------------------
""")
        wins = wins + 1
        #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #computer:rock / user:scissors
    elif cc == "r" and uc == "s":
        print(f"""
--------------------------
Computer Choice: Rock
User Choice: Scissors
--------------------------
You lose.
--------------------------
Wins: {wins}
Losses: {losses + 1}
--------------------------
""")
        losses = losses + 1
        #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #computer:paper / user:rock
    elif cc == "p" and uc == "r":
        print(f"""
--------------------------
Computer Choice: Paper
User Choice: Rock
--------------------------
You lose.
--------------------------
Wins: {wins}
Losses: {losses + 1}
--------------------------
""")
        losses = losses + 1
        #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #computer:paper / user:scissors
    elif cc == "p" and uc == "s":
        print(f"""
--------------------------
Computer Choice: Paper
User Choice: Scissors
--------------------------
You win!
--------------------------
Wins: {wins + 1}
Losses: {losses}
--------------------------
""")
        wins = wins + 1
                #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #computer:scissors / user:paper
    elif cc == "s" and uc == "p":
        print(f"""
--------------------------
Computer Choice: Scissors
User Choice: Paper
--------------------------
You lose.
--------------------------
Wins: {wins}
Losses: {losses + 1}
--------------------------
""")
        losses = losses + 1
        #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #computer:scissors / user:rock
    elif cc == "s" and uc == "r":
        print(f"""
--------------------------
Computer Choice: Scissors
User Choice: Rock
--------------------------
You win!
--------------------------
Wins: {wins + 1}
Losses: {losses}
--------------------------
""")
        wins = wins + 1
        #If user gets 5 wins stop the game
        if wins == 5:
            print("""
You beat the computer! You win.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        #if computer gets 5 wins stop the game
        elif losses == 5:
            print("""
The computer beat you! You lost.""")
            wins = 0
            losses = 0
            user_input = input("Would you like to play again? (y/n) :")
        else:
            user_input = "y"
    #any other answer
    else:
        print("Invalid input.")
        user_input = input("Would you like to play again? (y/n) :")

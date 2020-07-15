number = input("How many numbers? :")
placeholder = int(number)
user_input = "y"

#Run first round
for i in range(int(number)):
    print(i + 1)
#Ask user if they want to go again
confirmation = input("Would you like to continue? (y/n) :")
#Terminate program if no
if confirmation == "n":
    exit()
#Run it again with new inputs
elif confirmation == "y":
    while user_input == "y":
        number = input("How many numbers? :")
        #Set beginning and end of new range
        num1 = placeholder + 1
        num2 = int(number) + placeholder + 1
        for i in range(num1,num2):
            print(i)
        user_input = input("Would you like to continue? (y/n) :")
        if user_input == "n":
            exit()
        else:
            placeholder = num2 - 1

import random
import pandas as pd

# elements available for use in password
choice_container = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','!','@','#','$','%','&','*','-','+','=']

# get user inputs
print("""
Answer the following questions to recieve a randomly generated strong password.
""")
website = input("What website is this password for? :")
username = input("What is the username associated with this password? :")
user_input = input("Enter one word for the program to use in making your password. :")

# create a list of elements based on user input
input_elements = [letter for letter in user_input]
# create another list of random elements so that total elements equal 20
random_elements = [random.choice(choice_container) for letter in range(20-len(input_elements))]
# combine the two lists
combined = [random_elements.append(letter) for letter in input_elements]
#randomly shuffle elements
random.shuffle(random_elements)
#join the list to get a the finalized random password
password = "".join(element for element in random_elements)

# add information to dataframe
password_df = pd.read_csv("Resources/data.csv")
new_row = {"Website":website,"Username":username,"Password":password}
password_df = password_df.append(new_row, ignore_index=True)
# save information to csv
password_df.to_csv("Resources/data.csv", index=False)

print(f"Your new password is {password}")

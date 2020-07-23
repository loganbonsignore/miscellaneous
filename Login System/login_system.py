import os
import pandas as pd

def create_new_account(customer_df, private_df):
    # collect user information
    print("No Problem! Answer these questions to complete your account set up:")
    first_name = input("What is your first name? :")
    last_name = input("What is your last name? :")
    city = input("What city do you live in? :")
    phone = input("What is your phone number? :")
    email = input("What is your email address? :")
    username = input("What would you like your new username to be? :").lower()
    password = input("What would you like your new password to be? :")
    information = [first_name,last_name,city,phone,email]
    private = [username,password]
    # add new information to dataframe
    new_row = {"First Name":first_name,"Last Name":last_name,"City":city,"Phone":phone,"Email":email}
    customer_df = customer_df.append(new_row, ignore_index=True)
    # add new login info to private dataframe
    new_row_1 = {"Username":username,"Password":password}
    private_df = private_df.append(new_row_1, ignore_index=True)
    # save both dataframes to csv
    customer_df = customer_df.to_csv(customer_list_path, index=False)
    private_df = private_df.to_csv(private_path, index=False)
    print("Your account has been created!! Enjoy the benefits of our website")

# get resource file paths
customer_list_path = os.path.join("Resources/customer_list.csv")
private_path = os.path.join("Resources/private.csv")
# read csv
customer_list = pd.read_csv(customer_list_path)
private_list = pd.read_csv(private_path)
# create dataframes
customer_df = pd.DataFrame(customer_list)
private_df = pd.DataFrame(private_list)

# Ask user if they have an account
user_input = input("Do you have an account? (y/n) :")

# if the user has an account, prompt user to login
if user_input.lower() == "y":
    # ask user for username and password
    username = input("Enter your username :").lower()
    password = input("Enter your password :")
    # while the user is operating as a recognized username, check for the authenticity of their password
    while username.lower() in list(private_df["Username"]):
        # filter customer list dataframe to only the current user's information
        customer = private_df.loc[username==private_df["Username"],:]
        # authenticate username and password match
        if (username == customer["Username"]).bool() & (password == customer["Password"]).bool():
            print("Congratulations you're logged in")
            break
        # if password is incorrect ask user to re-enter password
        elif (username == customer["Username"]).bool() & (password != customer["Password"]).bool():
            password = input("That password is incorrect. Please try again.")
    # if username is not recognized, promt user to set up new account
    else:
        user_input = input("We don't have an account associated with that username. Would you like to set up a new account? (y/n)")
        # if user doesnt want to create new account, quit the program
        if user_input.lower() == "n":
            print("Thanks for visiting our website. We hope to hear from you again soon.")
            exit()
        # if user wants to create account, prompt them to set up a new account and collect information
        elif user_input.lower() =="y":
            create_new_account(customer_df, private_df)
# if user doesn't have an account, prompt them to set up a new account and collect information
elif user_input == "n":
    create_new_account(customer_df, private_df)

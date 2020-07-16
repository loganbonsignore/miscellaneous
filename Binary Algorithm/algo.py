import random
import numpy as np

random_array = random.choices(np.arange(0,100),k=50)
print(random_array)

# get user input
user_input = int(input("Enter a number between 1-100 for the algorithim to find :"))

# slice random_array array into two containers
middle_value = int(len(random_array)//2)
first_half = random_array[:middle_value]
second_half = random_array[middle_value:]

# confirm or deny user_input matches any element in the either container
if user_input in first_half:
    # split first_half container into two smaller containers
    middle_value = len(first_half)//2
    second_half = first_half[middle_value:]
    first_half = first_half[:middle_value]
    print(first_half)
    print(second_half)
elif user_input in second_half:
    # split second_half container into two smaller containers
    middle_value = len(second_half)//2
    first_half = second_half[:middle_value]
    second_half = second_half[middle_value:]
    print(first_half)
    print(second_half)
else:
    print("Your number is not in this list")
    exit()

# evaluate for match in new first_half container 
if user_input in first_half:
    # split new first_half container into two smaller containers
    middle_value = len(first_half)//2
    second_half = first_half[middle_value:]
    first_half = first_half[:middle_value]
    print(first_half)
    print(second_half)
# evaluate for match in new second_half container 
elif user_input in second_half:
    # split new second_half container into two smaller containers
    middle_value = len(second_half)//2
    first_half = second_half[:middle_value]
    second_half = second_half[middle_value:]
    print(first_half)
    print(second_half)

# evaluate for match in new first_half container 
if user_input in first_half:
    # split new first_half container into two smaller containers
    middle_value = len(first_half)//2
    second_half = first_half[middle_value:]
    first_half = first_half[:middle_value]
    print(first_half)
    print(second_half)
# evaluate for match in new second_half container 
elif user_input in second_half:
    # split new second_half container into two smaller containers
    middle_value = len(second_half)//2
    first_half = second_half[:middle_value]
    second_half = second_half[middle_value:]
    print(first_half)
    print(second_half)  

# check to see if number in first or second half of list
if user_input in first_half:
    # split new first_half container into two smaller containers
    middle_value = len(first_half)//2
    second_half = first_half[middle_value:]
    first_half = first_half[:middle_value]
    print(first_half)
    print(second_half)
# evaluate for match in new second_half container 
elif user_input in second_half:
    # split new second_half container into two smaller containers
    middle_value = len(second_half)//2
    first_half = second_half[:middle_value]
    second_half = second_half[middle_value:]
    print(first_half)
    print(second_half)

# check final numbers in first half
if (len(first_half)==1) and (first_half[0]==user_input):
        print(f"Your number, {first_half[0]}, is in this list.")
elif (len(first_half)==2) and (first_half[0]==user_input):
        print(f"Your number, {first_half[0]}, is in this list.")
elif (len(first_half)==2) and (first_half[1]==user_input):
        print(f"Your number, {first_half[1]}, is in this list.")
# check final numbers in second half       
elif (len(second_half)==1) and (second_half[0]==user_input):
    print(f"Your number, {second_half[0]}, is in this list.")
elif (len(second_half)==2) and (second_half[0]==user_input):
    print(f"Your number, {second_half[0]}, is in this list.")
elif (len(second_half)==2) and (second_half[1]==user_input):
    print(f"Your number, {second_half[1]}, is in this list.")

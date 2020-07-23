import random
import numpy as np
from sys import exit

def check_for_match(sorted_array, user_number):
    if len(sorted_array) == 1 or len(sorted_array) == 2:
        found = []
        for number in sorted_array:
            if number == user_number:
                print(f"We found your number {number}.")
                found.append(number)
                exit("Successful Exit^")
        if not found:
            print("We did not find your number.")
            exit("Successful Exit^^")
    elif len(sorted_array) == 0:
        print("We did not find your number.")
        exit("Successful Exit^^^")
        
def middle_index(sorted_array):
    index = len(sorted_array)//2
    return index

# Get user input for random array
start = int(input("Enter a start value for the random array :"))
stop = int(input("Enter an end value for the random array :"))

# Print array of numbers
k = (stop - start) // 2
random_array = random.choices(np.arange(start,stop),k=k)
print(random_array)

# Get user input
user_number = int(input("Enter a number for the computer to find :"))
# Safety net 'check for match' in case number of possible search results are limited
check_for_match(random_array, user_number)

# Sort random array
sorted_array = np.sort(random_array)

# While length of sorted_array is an even number, check for middle number match. If no match, remove middle number from array. 
while len(sorted_array)%2 == 0:
    if user_number == sorted_array[middle_index(sorted_array)]:
        print(f"We found your number {sorted_array[middle_index(sorted_array)]}.") 
        exit("Successful Exit*")
    elif user_number != sorted_array[middle_index(sorted_array)]:
        sorted_array = sorted_array[sorted_array != sorted_array[middle_index(sorted_array)]]    
# Iterate through sorted array until finding user's element or eliminating all possible options
while user_number != sorted_array[middle_index(sorted_array)]:
    print(f'Top of Algo Sorted Array: {sorted_array}') # for display purposes only
    # Create two halfs of the array
    half_1 = [sorted_array[x] for x in range(middle_index(sorted_array))]
    half_2 = [x for x in sorted_array if x not in half_1 and x != sorted_array[middle_index(sorted_array)]]
    # Compare user's number to the middle number of the array to decide which half of the array the user's number is more likley to be in
    if user_number > sorted_array[middle_index(sorted_array)]:
        new_half = half_2
    elif user_number < sorted_array[middle_index(sorted_array)]:
        new_half = half_1
    print(f'New Half: {new_half}') # for display purposes only
    # Sort newly chosen half to ensure accuracy
    sorted_array = np.sort(new_half)
    # If only a few elements in array, loop through the remaining elements to find a match or eliminate the possibility of a match.
    check_for_match(sorted_array, user_number)
    # While length of new array is an even number, check for middle number match. If no match, remove middle number from array. 
    while len(sorted_array)%2 == 0:
        if user_number == sorted_array[middle_index(sorted_array)]:
            print(f"We found your number {sorted_array[middle_index(sorted_array)]}.") 
            exit("Successful Exit**")
        else:
            sorted_array = sorted_array[sorted_array != sorted_array[middle_index(sorted_array)]]
            print(f'Even Converted Odd: {sorted_array}') # for display purposes only
    # If only a few elements in array, loop through the remaining elements to find a match or eliminate the possibility of a match.
    check_for_match(sorted_array, user_number)
    print("/NEW LOOP/") # for display purposes only
else:
    print(f"We found your number {sorted_array[middle_index(sorted_array)]}.")
    exit("Successful Exit***")
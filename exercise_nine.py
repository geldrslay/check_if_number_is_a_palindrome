# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse.

# Defining function
def palindrome (given_number):
    original_number = given_number
    print ("The given number is:", given_number)

    # Get the reverse of the given number.
    reverse_number = 0
    while given_number > 0:
        digit = given_number % 10
        reverse_number = digit + (reverse_number *10) 
       given_number = given_number // 10
    
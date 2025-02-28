# This assignment was to write a function that takes in a list of numbers and returns the sum of all the even numbers in the list.

listNum = [208,861,194,752,136,224,262,678,604,426,436,199,812,643,823,598,267.]
    
# iterating numbers in list
for num in listNum:

    # checking condition
    if num % 2 == 0:    #note to myself: I can target every third, forth etc. number by changing the num 
        print(num, end=" ")

# Resource for making this was: https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/

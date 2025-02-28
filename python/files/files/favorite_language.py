#   To remove whitespace from the string permanetly, you have to associate the stripped value with variable name:

favorite_language = "      Python "

favorite_language = favorite_language.strip()   #   Removes whitespace from all the sides
print(favorite_language)


#   To remove the whitespace from the string, you strip the whitespace from the right side of the string and then associate this new value with the original variable:

favorite_language.rstrip()   #  Removes the whitespace from right side
favorite_language.lstrip()   #  Remove the whitespace from left side

#   The stripping functions are used most often to clean up user input before it's stored in a program

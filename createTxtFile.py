# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
#   Created by Matteo Tramontina                  #
#   Date: 15 June 2022                            #
#   Version: 1.0                                  #
#   Github: https://github.com/tr4mo              #
#   Email: matteo.tramontina@outlook.com          #
#                                                 #
#   You can use this program for free, just       #
#   credit me if you use it for public purposes   #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #

# Get in input the string you want to write in the txt file
string = input("Type your string: ")

# This is the path where you want your file to be located
path = 'file.txt'

# Check if the path is correct, if not, send an error message
try:
    #                                  'w' if you want to rewrite the file everytime
    #                                  'a' if you want to append the string one row after
    #                                  'x' if you want to create a new file everytime (Watch out! This one can result in an error if you already have the file!)
    #        here   \ /   you can type:
    with open(path, 'w', encoding='utf-8') as f:
        # This is the point where you actually start typing the string in the file
        f.writelines(string)
except FileNotFoundError:
    # Do this if the given path doesn't exist
    print('Path ' + path + ' does not exist.')

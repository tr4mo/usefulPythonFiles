# # # # # # # # # # # # # # # # # # # # # # # # #
#   Created by Matteo Tramontina                #
#   Date: 15 June 2022                          #
#   Version: 1.0                                #
#   Github: https://github.com/tr4mo            #
#   Email: matteo.tramontina@outlook.com        #
#                                               #
#   You can use this program for free, just     #
#   credit me if you use it for public purposes #
#                                               #
# # # # # # # # # # # # # # # # # # # # # # # # #

string = input("Type your string: ")

path = 'file.txt'

try:
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(string)
except FileNotFoundError:
    print('Path ' + path + ' does not exist.')

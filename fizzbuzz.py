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

n = 100
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
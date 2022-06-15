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

# This is the number you want to elaborate
n = 100

# This loop iterates in a range 1 to n
for i in range(1,n+1):
    # If the number is divisible by 3 and by 5, print fizzbuzz
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    # If the number is divisible only by 3, print fizz
    elif i % 3 == 0:
        print("fizz")
    # If the number is divisible only by 5, print buzz
    elif i % 5 == 0:
        print("buzz")
    # If the number is not divisible by 3 or by 5, print the actual number
    else:
        print(i)

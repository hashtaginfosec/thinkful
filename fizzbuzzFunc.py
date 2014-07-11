"""
Write one function that determines if one number is evenly divisible by another and returns true or false
 Write another function that prints out the number/fizz/buzz/fizzbuzz as appropriate while iterating over an upper limit.
  This function should call the first one to test for each case (divisible by 5, 3, 15, etc.).
"""

from sys import argv


def evendivid(a, b):

    #print("Checking even divide \n")
    if a % b == 0:
        return True
    else:
        return False


#Write another function that prints out the number/fizz/buzz/fizzbuzz as appropriate while iterating over an upper
# limit. This function should call the first one to test for each case (divisible by 5, 3, 15, etc.).

def fizzbuzz(limit):

    for i in range(1, limit+1):
        if evendivid(i, 15) is True:
            print("test")
            print("fizz-buzz")
        elif evendivid(i, 3) is True:
            print("fizz")
        elif evendivid(i, 5) is True:
            print("buzz")
        else:
            print(i)


if __name__ == '__main__':

    if len(argv) == 2:
        filename, num = argv
        num = int(num)
    else:
        print("We need exactly 1 number. Using 20 for now. \n")
        num = 20

    #if evendivid(num1, num2):
    #    print("true xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    #let's find fizz-buzz numbers
    fizzbuzz(num)

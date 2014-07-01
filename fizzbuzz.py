#fizbuzz v2

import sys
num = 0

if len(sys.argv) <= 1:
    num = int(input("Please type upper limit >>> "))

else:
    for arg in sys.argv[1:]:
        num = int(arg)

print("Fizz buzz counting up to " + str(num))
for i in range(1, num+1):

    if i % 3 == 0 and i % 5 != 0:
        print("fizz")
    if i % 5 == 0 and i % 3 != 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)


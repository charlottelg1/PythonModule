import sys

if (len(sys.argv) == 1):
	exit()

if (len(sys.argv) > 2):
	print ("AssertionError: more than one argument are provided")
	exit()

if not sys.argv[1].isnumeric():
	print ("AssertionError: argument is not an integer")
	exit()

number = int(sys.argv[1])

if number == 0:
	print("I'm Zero.")

elif number % 2 == 0:
	print("I'm Even.")

else:
	print("I'm Odd.")




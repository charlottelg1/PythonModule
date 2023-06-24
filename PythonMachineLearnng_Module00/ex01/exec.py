import sys

if (len(sys.argv) == 1):
	exit()

argument = sys.argv[1]

if (len(sys.argv) > 2):
	i = 2
	while (i < len(sys.argv)):
		argument += ' '
		argument += sys.argv[i]
		i += 1

reverse = argument[::-1]
# print (reverse)
swap = reverse.swapcase()
print (swap)

import sys

try:
	assert len(sys.argv) != 1, """Usage: python operations.py <number1> <number2>
Example:
	python operatios.py 10 3"""
	assert len(sys.argv) < 4, "AssertionError: too many arguments"
	assert len(sys.argv) > 2, "AssertionError: too few arguments"

	try:	
		A = int(sys.argv[1])
		B = int(sys.argv[2])
	except ValueError:
		raise AssertionError("AssertionError: only integers")
		
except AssertionError as msg:
		print(msg)
		exit()
				


Sum = A+B
Diff = A-B
Prod = A*B
if B != 0:
	Quot = A/B
	Rem = A%B
else:
	Quot = "ERROR (divison by zero)"
	Rem = "ERROR (modulo by zero)"

table = {'Sum:': Sum, 'Difference:': Diff, 'Product': Prod, "Quotient:": Quot, "Remainder:": Rem}
for name, value in table.items():
	print(f'{name:15} {value}')


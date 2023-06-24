import string
import sys

def text_analyzer(arg=None):
	'''
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	'''
	
	try:
		assert arg!=None,"What is the text to analyze?"
		assert isinstance(arg, str), "AssertionError: argument is not a string"
	except AssertionError as msg:
			print(msg)
			return

	upper = 0
	lower = 0
	punct = 0
	space = 0
	
	for character in arg:
		if character.isupper():
			upper += 1 
		elif character.islower():
			lower += 1
		elif character.isspace():
			space +=1
		else:
			for sign in string.punctuation:
				if character == sign:
					punct += 1		
	print(f"""The text contains {upper+lower+space+punct} character(s):
- {upper} upper letter(s) 
- {lower} lower letter(s)
- {punct} punctuation mark(s)
- {space} space(s)""")
		
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("AssertionError: You should provide 1 argument, no more, no less")
		exit()
	text_analyzer(sys.argv[1])
import sys

CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

try:
    assert len(sys.argv) > 1, "[USAGE] Provide alphanumeric arguments to be encoded in Morse code"
    
except AssertionError as msg:
		print(msg)
		exit()
                
sys.argv.remove(sys.argv[0])

args_str = ' '.join([str(item) for item in sys.argv])

for char in args_str:
       	if not char.isalpha() and not char.isnumeric() and not char.isspace():
                print("ERROR")
                exit()

morse = ''

for char in args_str:
        if char.isspace():
                morse += '/ '
        else:
                morse += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '

print(morse)



                
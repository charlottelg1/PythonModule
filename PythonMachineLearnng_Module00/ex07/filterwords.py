import sys

try:
    assert len(sys.argv) == 3, "ERROR"
    assert type(sys.argv[1]) == str, "ERROR"
    assert sys.argv[2].isnumeric(), "ERROR" 
    
except AssertionError as msg:
		print(msg)
		exit()
                
str_to_list = sys.argv[1].split()

punc = ''',!()-[]{};:'"\,<>./?@#$%^&*_~'''

for i, x in enumerate(str_to_list):
        if x[-1] in punc:
                str_to_list[i] = x.replace(x[-1],"")
                
list_without_punct = [x for x in str_to_list if x.isalpha()] 
# only alpha char in word and get rid of punctuation

list_check_len = [x for x in list_without_punct if len(x) > int(sys.argv[2])]

print(list_check_len)
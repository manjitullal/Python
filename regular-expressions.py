import re
text = "abcdefgh 10"
text2 = "{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}"

#pattern = re.compile(r'abc') # match abc from the text
#pattern = re.compile('\d') # match a digit
#pattern = re.compile('\D') # match a not a digit
#pattern = re.compile('\w') # match a word character
#pattern = re.compile('\W') # match a not word character
#pattern = re.compile('\s') # match a space
#pattern = re.compile('\S') # match a not space
#^ start with something
#$ end with something
#. will match anything
#match only the character items in the set [-.]

pattern = re.compile(r"\'name\'..\'\w+\'")

matches = pattern.finditer(text2)

for match in matches:
    print(match)



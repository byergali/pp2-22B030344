import re

f = open('text.txt', encoding='utf-8')
s = str(f.read())

x = re.search("[a-z]+_[a-z]+", s)

if x:
    print("it's a match")
else:
    print("no match found")
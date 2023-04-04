# regular expressions are common to all programming languages

import re

pattern = re.compile('this')
string = 'search this inside of this text please'

'''print('search' in string)

print(re.search('this', string))
a = re.search('this', string)
span = a.span()
print(span)
start = a.start()
end = a.end()
gr = a.group()
print(gr)'''

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)

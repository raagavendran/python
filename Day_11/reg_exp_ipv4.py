import re

print 'enter strings with number'
st = raw_input()

p=re.compile(r'\d{1,2}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
f=re.findall(p,st)
print f 

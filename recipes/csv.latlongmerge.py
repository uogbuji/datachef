import sys
import re

#f = open('/Users/uche/Downloads/spotlight-sample.csv')
f = sys.stdin
#Regex for latitude,longitude
P = re.compile(',(-?[\d]{1,3}\.[\d\.]+,-?[\d]{1,3}\.[\d\.]+),')
lines = [ P.sub(lambda x: ',"' + x.group(1) + '",', l) for l in f ]

for l in lines: sys.stdout.write(l)

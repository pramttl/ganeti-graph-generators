'''
Code to create a JSON dump of the entire cluster graph.
'''

jsgraph = dict()

while True:
    s = raw_input()
    if s == '':
        break
    l = s.split()

    if l[2]:
        jsgraph[l[0]] = [l[1],l[2]]
    else:
        jsgraph[l[0]] = [l[1],]

from pprint import pprint as pp
#pp(jsgraph)

import simplejson as json
s = json.dumps(jsgraph)
pp(s)

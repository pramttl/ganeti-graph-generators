# 
# Code to read the raw Ganeti Cluster Graph and print the Graph in a format, required as per the arbor.js standards.
# $ python createarborgraph.py < ../test_graph.txt
# Pranjal Mittal
#

nodedict = {}
while True:
    s = raw_input()
    if s == '':
        break
    l = s.split()
    try:
        nodedict[l[1]]
        nodedict[l[1]].append(l[0])
    except KeyError:
        nodedict[l[1]] = [l[0],]


#from pprint import pprint as pp
#pp(nodedict)


# To print the nodes
for node in sorted(nodedict.keys()):
    s = '"%s":{color:CLR.ganetinode, shape:"dot", alpha:1},'%(node,)
    print s
    for instance in nodedict[node]:
        s = '"%s":{color:CLR.ganetivm, alpha:1},'%(instance,)
        print s
    print


# To print the edges.
for node in sorted(nodedict.keys()):
    s = '\t"%s":{'%(node,)
    print s
    for instance in nodedict[node]:
        s = '\t\t"%s":{length:2},'%(instance,)
        print s
    print '\t},'


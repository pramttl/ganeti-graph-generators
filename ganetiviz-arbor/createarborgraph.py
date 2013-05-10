# 
# Code to read the raw Ganeti Cluster Graph and print the Graph in a format, required as per the arbor.js standards.
# $ python createarborgraph.py < ../test_graph.txt
# Pranjal Mittal
#

# Dictionary which maps nodes to list of primary nodes. 
nodedict = {}

# Dictionary which maps "instance groups" (primary_nodes) to a dictionary of secondary nodes also having weights.
# Example : node1:{node3 : 5} => Means that 5 VMs having node1 as primary have node3 as secondary.
# The dictionary is a Directed Graph.
psdict = {}

while True:
    s = raw_input()
    if s == '':
        break
    l = s.split()

    ##Creating the PrimaryNode-Instance relations.
    try:
        nodedict[l[1]]
        nodedict[l[1]].append(l[0])
    except KeyError:
        nodedict[l[1]] = [l[0],]

    ##Creating the "instance-group" to secondary node relations.
    try:
        # p[1] might not be already there in psdict, thats why we "try" it.
        snodes = psdict[l[1]]
        # Increase count of no. of links from pnode to the respective snode.
        if l[2] in snodes:
            snodes[l[2]] += 1
        else:
            if l[2] != 'None':
                snodes[l[2]] = 1
    #This exception occurs only when l[1] not in psdict.
    except KeyError:
        if l[2] != 'None':
            psdict[l[1]] = {l[2]: 1}


from pprint import pprint as pp
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


pp(psdict)
print

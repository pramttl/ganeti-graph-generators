# 
# Code to read the raw Ganeti Cluster Graph and print the Graph in a format, required as per the arbor.js standards.
# $ python pygraph.py < ../graph_prod.txt
# Pranjal Mittal
#

# Dictionary which maps nodes to list of primary nodes. 
nodedict = {}

# Dictionary which maps "instance groups" (primary_nodes) to a dictionary of secondary nodes also having weights.
# Example : node1:{node3 : 5} => Means that 5 VMs having node1 as primary have node3 as secondary.
# The dictionary is a Directed Graph.
psdict = {}

import pickle
OBJECT_STORAGE_FILE = 'pickled_objects.txt'

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


# Pickling the nodedict,psdict object for the current user and storing it in a file.
f = open(OBJECT_STORAGE_FILE, 'w') 
pickle.dump(nodedict, f)
pickle.dump(psdict, f)
f.close()

from pprint import pprint as pp
#pp(nodedict)
#pp(psdict)
#print


# To print the nodes
i = 0
for node in sorted(nodedict.keys()):
    s = "{ data: { id: '%s', name: '%s', weight: 100,},"\
        "\n\tposition: pp[%d], classes:'ganeti-node' },"%(node,node,i)
    print s

    node_slug = node.split(".")[0]
    for instance in nodedict[node]:
        s = "{ data: { id: '%s', name: '%s', weight: 0.05,}," \
            "\n\tposition: rndisc(pp[%d],27,31)," \
            " classes:'ganeti-instance' },"%(instance,instance,i)
        print s
    print
    i += 1

'''
print "EDGES"
print "--------------------------------------------------------"
# To print the edges.
for node in sorted(nodedict.keys()):
    #Edges to Instances.
    for instance in nodedict[node]:
        s = "{ data: { source: '%s', target: '%s', faveColor: '#6FFCB1', strength:1 }, classes:'instance-edge'},"%(node,instance)
        print s

    ##Edges to Secondary Nodes.
    #for snode,slinkweight in psdict[node].items():
    #    s = '\t\t"%s":{length:15, width:%d},'%(snode,slinkweight)
    #    s = "{ data: { source: '%s', target: '%s', faveColor: '#6FB1FC', strength: %d }, classes:'snode-edge' },"%(node,snode,slinkweight)
    #    print s
    #print '\t},'


############################ Handy Functions ##############################

def js_nodes_obj(nodedict):

    #Takes in a "nodedict" and converts it into a Javascript Nodes object.
    
    s = '{\n'
    for node in sorted(nodedict.keys()):
        s += '"%s":{color:CLR.ganetinode, shape:"dot", alpha:1},\n'%(node,)
        for instance in nodedict[node]:
            s += '"%s":{color:CLR.ganetivm, alpha:0},\n'%(instance,)
        s += '}\n'
    return s


def js_edges_obj(nodedict,psdict):

    #Takes in "nodedict" and "psdict" dictionaries and uses it to 
    #generate a string representation of the Javascript EDGE object.

    s = '{\n'
    for node in sorted(nodedict.keys()):
        s += '\t"%s":{\n'%(node,)

        #Edges to Instances.
        for instance in nodedict[node]:
            s += '\t\t"%s":{length:6},\n'%(instance,)
        #Edges to Secondary Nodes.
        for snode,slinkweight in psdict[node].items():
            if snode:
                s += '\t\t"%s":{length:15, width:%d},\n'%(snode,slinkweight)
        s+='\t},\n'
    s+='}'
    return s


s = js_edges_obj(nodedict,psdict)
print s
'''

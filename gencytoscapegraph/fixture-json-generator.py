# 
# Code to read the raw Ganeti Cluster Graph and print the Graph in a format, required as per the arbor.js standards.
# $ python fixture-json-generator.py < ../graph_prod.txt
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
from simplejson import dumps

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


def gnodes_json_obj(nodedict):
    # Takes in a "nodedict" and converts it into a list of JSON objects representing ganeti nodes.
    gnodes_list = []
    i = 0
    for node_hostname in sorted(nodedict.keys()):
        i+=1
        gnode_obj = {}
        gnode_obj["pk"] = i
        gnode_obj["model"] = "ganeti_web.node"
        gnode_obj["fields"] = { "ram_free": 408,
                              "offline": "false",
                              "hostname": node_hostname,
                              "ram_total": 496,
                            }
        gnodes_list.append(gnode_obj)  
    return dumps(gnodes_list)

print gnodes_json_obj(nodedict)


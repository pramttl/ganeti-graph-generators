# 
# Code to read the raw Ganeti Cluster Graph and print JSON fixture data as output for "github.com/pramttl/ganetiviz-cytoscape" project.
# $ python fixture-json-generator.py < ../graph_prod.txt
# Pranjal Mittal
#

# Dictionary which maps nodes to list of primary nodes. 
nodedict = {}

# Dictionary mapping vm to list of 2 nodes, first being the primary node and the latter being the secondary node.
vmdict = {}


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


    ##Creating the PrimaryNode-Instance relations.
    vmdict[l[0]] = [l[1],l[2]]



def vms_json(vmdict):
    # Takes in a "vmdict" and converts it into a list of JSON objects representing ganeti nodes.
    vms_list = []
    i = 0
    for instance in sorted(vmdict.keys()):
        pnode = vmdict[instance][0]
        snode = vmdict[instance][1]
        i+=1
        vm_obj = {}
        vm_obj["pk"] = i
        vm_obj["model"] =  "ganeti_web.virtualmachine"
        vm_obj["fields"] = {
                            "status": "running",
                            "secondary_node": snode,
                            "hostname": instance,
                            "primary_node": pnode
                           }
        vms_list.append(vm_obj)  
    return dumps(vms_list)


def gnodes_json(nodedict):
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


print vms_json(vmdict)
#print gnodes_json(nodedict)


# To extract useful graph information from Ganeti Cluster (sanitized) JSON output.

import simplejson

# Select the cluster sanitized JSON file you wish to load.
f = open('prod.json')

cluster = simplejson.load(f)
instances = cluster['instances']

d = {}

for instance_name in instances:
    primary_node = instances[instance_name].get('primary_node')
    secondary_node = instances[instance_name].get('secondary_node')
    d[instance_name] = primary_node,secondary_node
    print instance_name,
    print primary_node,
    print secondary_node

#print simplejson.dumps(d)


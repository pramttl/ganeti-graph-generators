# To extract useful graph information from Ganeti Cluster JSON configuration file. (raw)
import simplejson
import sys
from collections import OrderedDict

DEFAULT_CONFIG_FILE = 'prod.json'

# Select the cluster sanitized JSON file you wish to load.
try:
    config_file = sys.argv[1]
    f = open(config_file)

#Opening the default json configuration file in case the user does not supply the config file name.
except IndexError:
    f = open(DEFAULT_CONFIG_FILE)


cluster = simplejson.load(f)
instances = cluster['instances']

print "Instance Name".ljust(27),
print "Primary Node".ljust(21),
print "Secondary node".ljust(21)
print "-"*68

d = {}

for iname in instances:
    instance_name = instances[iname]['name']
    primary_node = instances[instance_name].get('primary_node')
    logical_id = instances[instance_name].get('disks')[0].get('logical_id')

    #Setting Null default for secondary node.
    secondary_node = None
    if logical_id[0] == primary_node:
        secondary_node = logical_id[1]
    elif logical_id[1] == primary_node:
        secondary_node = logical_id[0]
    d[instance_name] = primary_node,secondary_node

    print instance_name.ljust(27),
    print primary_node.ljust(21),
    print secondary_node


#print simplejson.dumps(d)


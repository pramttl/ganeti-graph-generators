## Helper code to extract useful graph structures; used by supplementary graph visualization code.
<br/>

* To extract useful graph information from Ganeti Cluster JSON configuration file. (raw)
* To render the graph in suitable formats for use by dependent repositories.

### Utility Modules

> gencytoscapegraph

  Used to generate graph's useful to the Ganeti Cluster Mapping project. (which make use of Cytoscape JS) <br/>
  #TODO- Add link to repository.

> genarborgraph

  Used to generate graph's useful to the Ganeti Cluster Mapping project. (which make use of Arbor JS)
  See code for it [here](https://github.com/pramttl/ganetiviz-arbor)

> nxgraphview.py

  Used to visualize the Instance-Primary_Node relations in the Ganeti Cluster Graph using networkx and matplotlib.

### Notes

The code makes use of the sample OSUOSL cluster configuration JSON made avaialbe by @ramereth, 
courtsey [OSUOSL](http://github.com/osuosl).
The purpose of this repository is to support the dependent repositories, as a rapid development and testing framework.
Dependent Ganeti Graph Visuzaliation projects-

* ganetiviz-arbor
* ganetiviz-cytoscape


## Copyright

This work is licensed under a [Creative Commons Attribution-Share Alike 3.0
United States License](http://creativecommons.org/licenses/by-sa/3.0/us/).

vi: set tw=80 ft=markdown :

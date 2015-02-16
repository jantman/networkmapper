#!/usr/bin/env python

# requires pydot >= 1.0.28; pip sees this as external and unverified
import pydot
import json

graph = pydot.Dot(graph_name='network', graph_type='graph', size='80, 80', overlap="scale")

json_nodes = []
json_links = []

nodes = {}
nodes['core1'] = pydot.Node('core1', style='filled', fillcolor='red')
graph.add_node(nodes['core1'])
json_nodes.append({'name': 'core1'})
nodes['core2'] = pydot.Node('core2', style='filled', fillcolor='red')
graph.add_node(nodes['core2'])
json_nodes.append({'name': 'core2'})


def make_edge_label(s):
    return s

graphdata = {}
for i in range(17):
    switchname = 'switch{i}'.format(i=i)
    nodes[switchname] = pydot.Node(switchname, style='filled', fillcolor='yellow')
    graph.add_node(nodes[switchname])
    json_nodes.append({'name': switchname})
    idx = json_nodes.index({'name': switchname})
    graph.add_edge(pydot.Edge(nodes['core1'], nodes[switchname], label=make_edge_label('uplink'), color='green'))
    json_links.append({'source': 0, 'target': idx})
    graph.add_edge(pydot.Edge(nodes['core2'], nodes[switchname], label=make_edge_label('uplink'), color='green'))
    json_links.append({'source': 1, 'target': idx})
    for x in range(20):
        devname = 'switch{i}dev{x}'.format(i=i, x=x)
        nodes[devname] = pydot.Node(devname)
        graph.add_node(nodes[devname])
        json_nodes.append({'name': devname})
        idx2 = json_nodes.index({'name': devname})
        graph.add_edge(pydot.Edge(nodes[switchname], nodes[devname], label=make_edge_label('uplink'), color='blue'))
        json_links.append({'source': idx, 'target': idx2})
        if x % 10 == 0:
            graph.add_edge(pydot.Edge(nodes[switchname], nodes[devname], label=make_edge_label('uplink'), color='blue'))
            json_links.append({'source': idx, 'target': idx2})

j = {'nodes': json_nodes, 'links': json_links}
with open('graph.json', 'w') as fh:
    fh.write(json.dumps(j))
print("Graph written to: graph.json")

graph.write_dot('netgraph.dot')
for p in ['dot', 'neato', 'sfdp', 'fdp', 'twopi', 'circo']:
    for t in ['png', 'svg']:
        fname = 'netgraph_{p}.{t}'.format(p=p, t=t)
        print("writing {f}".format(f=fname))
        graph.write(fname, prog=p, format=t)

"""
clusters - see http://jseabold.net/blog/2012/02/12/making-graphical-models-with-pydot/
http://daft-pgm.org/
LANL routes - http://networkx.lanl.gov/examples/drawing/lanl_routes.html
http://graph-tool.skewed.de/

some graphviz examples: http://www.poirrier.be/~jean-etienne/articles/graphviz/

Other tech:
d3.js:
http://bl.ocks.org/mbostock/4063550
http://bost.ocks.org/mike/fisheye/ - fisheye distortion
http://www.redotheweb.com/CodeFlower/
http://www.whodotheyserve.com/ - big data viz with highlighting and links - source: https://github.com/dizzib/WhoDoTheyServe.com
http://nlpviz.bpodgursky.com/home - draggable tree diagram
http://charts.animateddata.co.uk/datavistree/ - collapsable tree
d3.js export - http://d3export.housegordon.org/
http://js.cytoscape.org/
OpenNMS info - http://www.opennms.org/wiki/Topology_Maps

http://nylen.tv/d3-process-map/graph.php - from https://github.com/nylen/d3-process-map
draggable - http://fatiherikli.github.io/programming-language-network/#language:C++

d3 interoperability tools - https://github.com/mbostock/d3/wiki/Gallery#interoperability
https://gist.github.com/plandem/5683951

http://felix-kling.de/JSNetworkX/examples.html - undirected weighted example
http://sigmajs.org/
http://js.cytoscape.org/
http://community.wolfram.com/groups/-/m/t/423070?p_p_auth=cDUnsWU5

drag and zoom - http://bl.ocks.org/mbostock/3681006 ; http://stackoverflow.com/questions/26538268/d3-js-network-diagram-zoom


"""

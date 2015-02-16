networkmapper
==============

.. image:: http://www.repostatus.org/badges/0.1.0/concept.svg
   :alt: Project Status: Concept - Minimal or no implementation has been done yet.
   :target: http://www.repostatus.org/#concept

Set of tools to map data networks (physical layer).

This is a problem I've tried to solve a number of times, but never found a good
solution to. Right now, this is just a concept...

* Store elements (nodes and edges) in a graph database.
* ReST API to update nodes and connections - separate tooling to
  collect data and do the mapping.
* Nodes are associated via "unique IDs" - i.e. MAC addresses on a switch,
  virtualization domain IDs, etc.; we create an edge by finding two nodes
  with matching unique IDs. A unique ID can also have an edge label, such
  as an interface or port number. The idea here is to allow data collection
  to do its job - i.e. list the ports on a switch and the MAC addresses
  on each port, or the running VMs on a hypervisor and their unique
  IDs - and then handle correlating nodes and creating the edges between
  them in the graph database, where this is done easily.
* Web interface - probably d3.js-based:
  * show complete graph (map) with edges
  * edge labels for interface/logical connection point at each end, and
    transport method/bandwidth/etc. in between
  * ability to show only or filter out a given set of nodes
  * ability to show or hide edge labels
  * each node and edge can have multiple URLs with a popup
  * ability to zoom and drag map
  * export to SVG, and to print-optimized file
  * ability to select N nodes and show all possible paths between them
  * printable view show have an index of all nodes, and what nodes they're
    connected to
  * show age of data

Examples
---------

* `OpenNMS <http://www.opennms.org>`_ is AGPL 3 and has a nice interactive
  `topology map <http://demo.opennms.com/opennms/topology>`_ (demo:demo). The frontend is
  `based on <http://www.opennms.org/wiki/Topology_Maps>`_ D3.js and SVG, but it seems like
  most of the calculation is done on the backend using a Vaadin OSGi app. The
  `code <https://github.com/OpenNMS/opennms/tree/develop/features/topology-map>`_ for this
  seems quite complex, and seems to do the graph-building server-side.

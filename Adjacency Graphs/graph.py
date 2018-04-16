# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from array_queue import ArrayQueue

class Graph:
  """Representation of a simple graph using an adjacency map."""

  #------------------------- nested Vertex class -------------------------
  class Vertex:
    """Lightweight vertex structure for a graph."""
    __slots__ = '_element'
  
    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      self._element = x
  
    def element(self):
      """Return element associated with this vertex."""
      return self._element
  
    def __hash__(self):         # will allow vertex to be a map/set key
      return hash(id(self))

    def __str__(self):
      return str(self._element)

    def __eq__(self, other):
      return str(self)==str(other)

    def __repr__(self):
      return str(self._element)
    
  #------------------------- nested Edge class -------------------------
  class Edge:
    """Lightweight edge structure for a graph."""
    __slots__ = '_origin', '_destination', '_element'
  
    def __init__(self, u, v, x):
      """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
      self._origin = u
      self._destination = v
      self._element = x
  
    def endpoints(self):
      """Return (u,v) tuple for vertices u and v."""
      return (self._origin, self._destination)
  
    def opposite(self, v):
      """Return the vertex that is opposite v on this edge."""
      if not isinstance(v, Graph.Vertex):
        raise TypeError('v must be a Vertex')
      return self._destination if v is self._origin else self._origin
      raise ValueError('v not incident to edge')
  
    def element(self):
      """Return element associated with this edge."""
      return self._element
  
    def __hash__(self):         # will allow edge to be a map/set key
      return hash( (self._origin, self._destination) )

    def __str__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
    
    def __eq__(self, other):
      return str(self)==str(other)

    def __repr__(self):
      return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
    
  #------------------------- Graph methods -------------------------
  def __init__(self, directed=False):
    """Create an empty graph (undirected, by default).

    Graph is directed if optional paramter is set to True.
    """
    self._outgoing = {}
    # only create second map for directed graph; use alias for undirected
    self._incoming = {} if directed else self._outgoing
    self.directed = directed

  def _validate_vertex(self, v):
    """Verify that v is a Vertex of this graph."""
    if not isinstance(v, self.Vertex):
      raise TypeError('*Vertex expected')
    if v not in self._outgoing:
      raise ValueError('*Vertex does not belong to this graph.')


  def _validate_edge(self, e): #validating the edge
    """Verify that e is an Edge of this graph."""
    if not isinstance(e, self.Edge):
      raise TypeError('*Edge expected')
    
  def is_directed(self):
    """Return True if this is a directed graph; False if undirected.

    Property is based on the original declaration of the graph, not its contents.
    """
    return self._incoming is not self._outgoing # directed if maps are distinct

  def vertex_count(self):
    """Return the number of vertices in the graph."""
    return len(self._outgoing)

  def vertices(self):
    """Return an iteration of all vertices of the graph."""
    return self._outgoing.keys()

  def edge_count(self):
    """Return the number of edges in the graph."""
    total = sum(len(self._outgoing[v]) for v in self._outgoing)
    # for undirected graphs, make sure not to double-count edges
    return total if self.is_directed() else total // 2

  def edges(self):
    """Return a set of all edges of the graph."""
    result = set()       # avoid double-reporting edges of undirected graph
    for secondary_map in self._outgoing.values():
      result.update(secondary_map.values())    # add edges to resulting set
    return result

  def get_edge(self, u, v):
    """Return the edge from u to v, or None if not adjacent."""
    self._validate_vertex(u)
    self._validate_vertex(v)
    return self._outgoing[u].get(v)        # returns None if v not adjacent

  def degree(self, v, outgoing=True):   
    """Return number of (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to count incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    return len(adj[v])

  def incident_edges(self, v, outgoing=True):   
    """Return all (outgoing) edges incident to vertex v in the graph.

    If graph is directed, optional parameter used to request incoming edges.
    """
    self._validate_vertex(v)
    adj = self._outgoing if outgoing else self._incoming
    for edge in adj[v].values():
      yield edge

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = self.Vertex(x)
    self._outgoing[v] = {}
    if self.is_directed():
      self._incoming[v] = {}        # need distinct map for incoming edges
    return v
      
  def insert_edge(self, u, v, x=None):
    """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
    if self.get_edge(u, v) is not None:      # includes error checking
      raise ValueError('u and v are already adjacent')
    e = self.Edge(u, v, x)
    self._outgoing[u][v] = e
    self._incoming[v][u] = e


  def remove_vertex(self, v):
    """Remove the vertex v and all its incident edges,
    and return the vertex been removed.

    Parameter v is an instance of Vertex
    Algorithm should run in O(deg(v)) time
    """

    self._validate_vertex(v) #validating vertex u

    edges = list(self.incident_edges(v, False)) if self.directed else list(self.incident_edges(v))

    for edge in edges: #deleting incident edges of v
       self.remove_edge(edge) #removing each edge

    del self._outgoing[v] #deleting the vertex

    return v


  def remove_edge(self, e):
    """remove the edge e from the adjacency map for each
    incident vertex, and return the edge removed.

    Parameter e is an instance of Edge
    Algorithm should run in O(1) time.
    """ 
    
    self._validate_edge(e) #validating the receive edge

    u,v = e.endpoints() #getting the endpoints from edge instance

    self._validate_vertex(u) #validating vertex u
    self._validate_vertex(v) #validating vertex v

    #deleting the v to u edge if it undirected graph, and if edge v to u exists on this undirected graph
    if not self.directed and self._outgoing[v][u]: 
      del self._outgoing[v][u]

    del self._outgoing[u][v] #deleting the edge received

    return e

  def bfs_traversal(self):
    """implement a Breadth-First Search method inside the
    class Graph, use a FIFO queue rather than a level-by-level formulation
    to manage vertices that have been discovered until the time when their
    neighbors are considered. Return a map of vertices and the edges that
    those vertices are discovered.
    """

    try: 
      key,v  = next(iter (self._outgoing.items()))   #Gettig the starting key

      print ("the starting vetrice = " , key)    #displaying the starting vertice
      self.empty = ArrayQueue()                      #creating empty queue to enqueue and dequeue
      visited = []                     #Empty list to keep track of the visited vertices 

      visited.append(key)           #Adding the starting Vertex to queue   
      self.empty.enqueue(key)              # Adding the starting Vertex to visited list

          
      print(key , "     " , None)    #The first  vertice is visited by none
    
      while self.empty._size > 0:              #checking the length of the queue
        key = self.empty.dequeue()        #setting the pointer node
             
        for x in (self.incident_edges(key)): #getting incident edges for vertex
          other_end = x.opposite(key)       #getting the opposite vertice on that edge  
     
          if other_end not in visited:           #checking if the vertex has been visited
            
            print (other_end, "     ", (key, other_end, x.element()))  #printing when the vertex was discovered 
            self.empty.enqueue(other_end)     #appending the both the queue and cisited list 
            visited.append(other_end)   
    
    except TypeError:
      print ("The vortex doesn't exit.") 


      

  def print_graph(self):
    """this method should print all vertices with their
    incident edges.
    """
    if len(self._outgoing ) > 0: 

      for key, nested in self._outgoing.items():
        print(key, list(nested.values()))
    
    else: 
      raise ValueError
#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

#  Nirdesh Bhandari & Siddharth Sudeer
# Project 3 - Final Project

from graph import Graph

def graph_from_edgelist(E, directed=False):
  """Make a graph instance based on a sequence of edge tuples.

  Edges can be either of from (origin,destination) or
  (origin,destination,element). Vertex set is presume to be those
  incident to at least one edge.

  vertex labels are assumed to be hashable.
  """
  g = Graph(directed)
  V = set()
  for e in E:
    V.add(e[0])
    V.add(e[1])

  verts = {}  # map from vertex label to Vertex instance
  for v in V:
    verts[v] = g.insert_vertex(v)

  for e in E:
    src = e[0]
    dest = e[1]
    element = e[2] if len(e) > 2 else None
    g.insert_edge(verts[src],verts[dest],element)

  return g

def graph_undirected(directed=False):
  """Return the weighted, undirected graph from project3.pdf (Diagram 1)"""
  
  E = (
  ('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3), ('A', 'E', 4), #A to B,C,D,E
    ('B', 'C', 5),                        #B to C
    ('C', 'D', 6), ('C', 'E', 7),               #C to D,E
    )
  return graph_from_edgelist(E, False) #setting directed to false

def graph_directed(directed=True):
  """Return the weighted, directed graph from project3.pdf (Diagram 2)"""
  E = (
  ('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3),  #A to B,C,D
    ('C', 'B', 5), ('C', 'D', 6), ('C', 'E', 7),  #C to B,D,E
    ('E', 'A', 4),                  #E to A
    )
  return graph_from_edgelist(E, True) #setting directed to true

def graph_empty(directed=False):
  """Return the weighted, undirected graph from project3.pdf (Diagram 1)"""
  
  E = ()
  return graph_from_edgelist(E, False) #setting directed to false

if __name__ =='__main__':

  # ==================================
  #  Creating Graph
  # ==================================

  #Creating Instances of Graphs
  g1 = graph_undirected()
  g2 = graph_directed()
  g3 = graph_empty()

  print("""\n========================================================
____ _ _  _ ____ _       ___  ____ ____  _ ____ ____ ___ 
|___ | |\ | |__| |       |__] |__/ |  |  | |___ |     |  
|    | | \| |  | |___    |    |  \ |__| _| |___ |___  |

========================================================
UNDIRECTED GRAPH
========================================================\n""")
  
  try :
    print("Undirected Original Graph:")
    g1.print_graph()
    print("\nNumber of vertices is", g1.vertex_count())
    print("Number of edges is", g1.edge_count())
    print("----------------------------------\n")
   
    print("BFS Traversal:")
    g1.bfs_traversal()
    print("----------------------------------\n")

    vertDEL = ''

    for vertex in g1.vertices(): 
      if vertex.element() == 'D': #searching for this vertex in all vertices
        vertDEL = vertex #assigning this vertex object to variable vertexDEL to pass to fxn
    try:
      g1.remove_vertex(vertDEL) #deleting vertex
      print("We have Removed Vertex: ", vertDEL, "\n")
      print("After Removing Vertex, Graph is:")
      g1.print_graph()
      print("\nNumber of vertices is now", g1.vertex_count())
      print("Number of edges is", g1.edge_count())
      print("----------------------------------\n")
    except Exception as err:
      print (err)
      print("----------------------------------\n")


    edgeDEL = object

    for edge in g1.edges():
      if edge == '(B,C,5)': #searching for this edge in all edges
        edgeDEL = edge #assigning this edge object to variable edgeDEL to pass to fxn

    try:
      g1.remove_edge(edgeDEL) #deleting edge
      print("We have Removed Edge: ", edgeDEL, "\n")
      print("After Removing Edge, Graph is:")
      g1.print_graph()
      print("\nNumber of vertices is now", g1.vertex_count())
      print("Number of edges is", g1.edge_count())
      print("----------------------------------\n")
    except Exception as err:
      print (err)
      print("----------------------------------\n") 

  except ValueError:
    print (" No Undirected graph exists.")

  print("========================================================")
  print("DIRECTED GRAPH")
  print("========================================================\n")

  try:
    print("Directed Original Graph:")
    g2.print_graph()
    print("\nNumber of vertices is", g2.vertex_count())
    print("Number of edges is", g2.edge_count())
    print("----------------------------------\n")


    print("BFS Traversal:")
    g2.bfs_traversal()
    print("----------------------------------\n")

    vertDEL = ''

    for vertex in g2.vertices():
      if vertex == 'D':
        vertDEL = vertex
    try:
      g2.remove_vertex(vertDEL)
      print("We have Removed Vertex: ", vertDEL, "\n")
      print("After Removing Vertex, Graph is:")
      g2.print_graph()
      print("\nNumber of vertices is now", g2.vertex_count())
      print("Number of edges is", g2.edge_count())
      print("----------------------------------\n")
    except Exception as err:
        print (err)
        print("----------------------------------\n")


    edgeDEL = object

    for edge in g2.edges():
      if edge == '(C,B,5)':
        edgeDEL = edge

    try:
      g2.remove_edge(edgeDEL)
      print("We have Removed Edge: ", edgeDEL, "\n")
      print("After Removing Edge, Graph is:")
      g2.print_graph()
      print("\nNumber of vertices is now", g2.vertex_count())
      print("Number of edges is", g2.edge_count())
      print("----------------------------------\n")
    except Exception as err:
        print (err)
        print("----------------------------------\n")
  except ValueError:
    print ("No Directed graph exists.")

  print("========================================================")
  print("PASSING EMPTY GRAPH (TESTING)")
  print("========================================================\n")
  
  try :
    print("Undirected Original Graph:")
    g3.print_graph()
    print("\nNumber of vertices is", g3.vertex_count())
    print("Number of edges is", g3.edge_count())
    print("----------------------------------\n")
   
    print("BFS Traversal:")
    g3.bfs_traversal()
    print("----------------------------------\n")

    vertDEL = ''

    for vertex in g1.vertices(): 
      if vertex.element() == 'D': #searching for this vertex in all vertices
        vertDEL = vertex #assigning this vertex object to variable vertexDEL to pass to fxn
    try:
      g3.remove_vertex(vertDEL) #deleting vertex
      print("We have Removed Vertex: ", vertDEL, "\n")
      print("After Removing Vertex, Graph is:")
      g3.print_graph()
      print("\nNumber of vertices is now", g3.vertex_count())
      print("Number of edges is", g3.edge_count())
      print("----------------------------------\n")
    except Exception as err:
      print (err)
      print("----------------------------------\n")


    edgeDEL = object

    for edge in g1.edges():
      if edge == '(B,C,5)': #searching for this edge in all edges
        edgeDEL = edge #assigning this edge object to variable edgeDEL to pass to fxn

    try:
      g3.remove_edge(edgeDEL) #deleting edge
      print("We have Removed Edge: ", edgeDEL, "\n")
      print("After Removing Edge, Graph is:")
      g3.print_graph()
      print("\nNumber of vertices is now", g3.vertex_count())
      print("Number of edges is", g3.edge_count())
      print("----------------------------------\n")
    except Exception as err:
      print (err)
      print("----------------------------------\n") 

  except ValueError:
    print (" No Undirected graph exists.")


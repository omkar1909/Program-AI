from collections import deque

# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
# Function to perform DFS traversal recursively on the graph 
def recursiveDFS(graph, v, discovered):
 
    discovered[v] = True            # mark the current node as discovered
    print(v, end=' ')               # print the current node
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:       # if `u` is not yet discovered
            recursiveDFS(graph, u, discovered)
 
# Function to perform BFS traversal recursively on the graph
def recursiveBFS(graph, q, discovered):
 
    if not q:
        return
 
    # dequeue front node and print it
    v = q.popleft()
    print(v, end=' ')
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            # mark it as discovered and enqueue it
            discovered[u] = True
            q.append(u)
 
    recursiveBFS(graph, q, discovered)

if __name__ == '__main__':
 
    # -----------------------------------------------------------------------
    # DFS starts here 
    
    # Creating an undirected graph for DFS
    edges1 = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
    
    # For DFS, total number of nodes in the graph (labelled from 0 to 12)
    n1 = 13
    
    # For DFS, build a graph from the given edges
    graph1 = Graph(edges1, n1)
 
    # For DFS, to keep track of whether a vertex is discovered or not
    discovered1 = [False] * n1
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    
    print("The DFS traversal (recursive) of given undirected graph is : ", end="\n")
    for i in range(n1):
        if not discovered1[i]:
            recursiveDFS(graph1, i, discovered1)
    
    # ------------------------------------------------------------------------
    # BFS starts below 
    
    # Create an undirected graph for BFS
    edges2 = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]
    
    # For BFS, total number of nodes in the graph (labelled from 0 to 14)
    n2 = 15
        
    # For BFS, build a graph from the given edges
    graph2 = Graph(edges2, n2)
    
    # For BFS, to keep track of whether a vertex is discovered or not
    discovered2 = [False] * n2

    # create a dequeue for doing BFS
    q = deque() 
    
    print("\n\nThe BFS traversal (recursive) of given undirected graph is : ", end="\n")
    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n2):
        if not discovered2[i]:
            # mark the source vertex as discovered
            discovered2[i] = True
 
            # enqueue source vertex
            q.append(i)
 
            # start BFS traversal from vertex i
            recursiveBFS(graph2, q, discovered2)
'''
TODO
Need to figure out how to use these classes to implement graoh
'''
#class for vertex and edges of a graph
#a class for the list of vertices
class graph():
    def __init__(self, nodes=[]):
        self.nodes=nodes


#a class for the list of edges/children of a vertex
class Node():
    def __init__(self, name, children=None):
        self.name=name
        self.children=children



#a more simplar way of representating a graph is adjacency matrix
#we need to keep a track of the nodes visted since graphs can have cycles, so visited is used for that

def dfs(node, visited=None):
    if node==None:
        return
    visited.add(node)
    print(node)
    if gr.get(node):
        for n in gr.get(node):
            if n not in visited:
                dfs(n,visited)
#traversing the graph in page 107 (also saved the picture in the directory titled "graph_Pg107"
gr={'0':['1','4','5'],'1':['3','4'],'2':['1'],'3':['2','4'],'4':[],'5':[]}
v=set()
'''
dfs(list(gr.keys())[0],v)
0
1
3
2
4
5
'''

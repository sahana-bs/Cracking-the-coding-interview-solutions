'''
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

bfs implementation is done
#TODO: dfs


TC:
similar to bfs base implementation.
'''
'''
#let us use dfs for this
def dfs_routefind(node1, node2, visited, gr):

    if node1==node2:
        print("Yes, a route exists")
        sys.exit()

    #if a route does not exist
    if len(visited)==len(gr.keys()):
        print("No route between the nodes")
        sys.exit()

    if node1==None:
        return

    visited.add(node1)
    if gr.get(node1):
        for n in gr.get(node1):
            if n not in visited:
                DoesPathExist(n,node2,visited,gr)

'''
#even bfs can be used to implement this
def bfs_routefind(node1, node2, visited=None, q=None, gr=None):
    if node2==None:
        return
    #edge cases, both nodes do not lead anywhere
    if (gr.get(node1)==[] and gr.get(node2)==[]) or (gr.get(node1)==[]):
        print("No route")
        return
    #fill the queue with the root nodes children
    visited.add(node1)
    for item in gr.get(node1):
        q.append(item)
    while q:
        node = q[0]
        if node not in visited:
            if node==node2:
                print("Yes, there's a route")
                break
            visited.add(node)
            #print(node, end=' ')
            for item in gr.get(node):
                q.append(item)
        #node already visited, remove from queue
        q=q[1:]
    #print("No route between the two nodes")




gr={'0':['1','4','5'],'1':['3','4'],'2':['1'],'3':['2','4'],'4':[],'5':[]}
v=set()
q = []
node1 = '0'
node2 = '2'
bfs_routefind(node1, node2, v, q, gr)
